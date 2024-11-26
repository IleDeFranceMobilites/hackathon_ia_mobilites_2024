import {Annotation, END, LangGraphRunnableConfig, Send, START, StateGraph} from "@langchain/langgraph";
import {Document} from "@langchain/core/documents";
import {z} from "zod";

import {llm} from "../../registry/registry";
import {vectorStore} from "../../rag/elastic";
import {getDefaultPromptConfig} from "../rag/prompts";

export const ResearcherGraphAnnotation = Annotation.Root({
  question: Annotation<string>,
  queries: Annotation<string[] | undefined>,
  documents: Annotation<Document[]>({
      reducer: (state: Document[], update: Document[]) => state?.concat(update),
      default: () => [],
    }
  )
});

export type ResearcherGraphReturnType = Partial<
  typeof ResearcherGraphAnnotation.State
>;

interface QueryState {
  query: string;
}


/**
 * Generate search queries based on the question.
 */
export const generateQueries = async (state: typeof ResearcherGraphAnnotation.State): Promise<ResearcherGraphReturnType> => {
  const modelWithTool = llm.withStructuredOutput(
    z.object({
      queries: z.array(z.string())
        .describe("List of generated search queries")
        .max(3)
    }),
    {name: "generate_queries"}
  );

  const messages = [
    {role: "system", content: getDefaultPromptConfig().generateQueriesSystemPrompt},
    {role: "human", content: state.question}
  ];

  const response = await modelWithTool.invoke(messages);

  return {queries: response.queries};
};

/**
 * Retrieve documents based on a given query.
 */
export const retrieveDocuments = async (
  state: QueryState,
  config: LangGraphRunnableConfig
): Promise<ResearcherGraphReturnType> => {
  const retriever = await makeRetriever(config);
  const response = await retriever.retrieve(state.query, config);
  return {documents: response};
};

const retrieveInParallel = (state: typeof ResearcherGraphAnnotation.State) => {
  if (!state.queries) {
    throw new Error("No queries found in state");
  }

  return state.queries.map(
    (query) => new Send("retrieveDocuments", {query})
  );
};

// Utility function to make retriever (implementation would depend on your retrieval system)
const makeRetriever = async (config: LangGraphRunnableConfig) => {
  return {
    retrieve: async (query: string, config: LangGraphRunnableConfig): Promise<Document[]> => {
      return vectorStore.similaritySearch(query, 5)
    }
  };
};


// Build the graph
const builder = new StateGraph(ResearcherGraphAnnotation)
  .addNode("generateQueries", generateQueries)
  .addEdge(START, "generateQueries")
  .addNode("retrieveDocuments", retrieveDocuments)
  .addConditionalEdges(
    "generateQueries",
    retrieveInParallel,
    ["retrieveDocuments"]
  )
  .addEdge("retrieveDocuments", END)

// Export the compiled graph
export const researcherGraph = builder.compile()
  .withConfig({
    maxConcurrency: 5
  });
