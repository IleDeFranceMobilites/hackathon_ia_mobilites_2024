FROM ubuntu:latest

# Set the same wd as in the devcontainer.json
WORKDIR /workspaces/idfm_hackaton_2024
COPY . .

# Install minimal dependencies
RUN apt-get update && apt-get install -y curl unzip git gcc

# Install 'task'
RUN chmod +x .infra/assets/task_install.sh && bash .infra/assets/task_install.sh -d -b /usr/local/bin
RUN task install

# Uncomment when ready to CD/CI
#CMD task dbt_run_full_refresh
