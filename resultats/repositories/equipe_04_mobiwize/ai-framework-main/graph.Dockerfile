# Use LangGraph.js API as base image
FROM langchain/langgraphjs-api:20 AS base

# Install pnpm and turbo globally
RUN npm install turbo --global
RUN pnpm config set store-dir ~/.pnpm-store

# Prune projects stage
FROM base AS pruner
ARG PROJECT=graph-api

WORKDIR /app
COPY . .
RUN turbo prune --scope=${PROJECT} --docker

# Build stage
FROM base AS builder
ARG PROJECT=graph-api

WORKDIR /app

# Copy lockfile and package.json's of isolated subworkspace
COPY --from=pruner /app/out/pnpm-lock.yaml ./pnpm-lock.yaml
COPY --from=pruner /app/out/pnpm-workspace.yaml ./pnpm-workspace.yaml
COPY --from=pruner /app/out/json/ .

# Install dependencies using cache mount
RUN --mount=type=cache,id=pnpm,target=~/.pnpm-store pnpm install --frozen-lockfile

# Copy source code of isolated subworkspace
COPY --from=pruner /app/out/full/ .

# Remove development dependencies
RUN --mount=type=cache,id=pnpm,target=~/.pnpm-store pnpm prune --prod --no-optional

# Final stage
FROM langchain/langgraphjs-api:20 AS runner

WORKDIR /app

# Copy the built application
COPY --from=builder /app .

# Set working directory to the project directory
WORKDIR /app/apps/graph-api

# Set environment variables
ENV NODE_ENV=production
ENV PORT=8000
ENV HOST="0.0.0.0"

EXPOSE ${PORT}

# Use the uvicorn command for the API server
CMD exec uvicorn langgraph_api.server:app --log-config /api/logging.json --host ${HOST} --port ${PORT} --no-access-log
