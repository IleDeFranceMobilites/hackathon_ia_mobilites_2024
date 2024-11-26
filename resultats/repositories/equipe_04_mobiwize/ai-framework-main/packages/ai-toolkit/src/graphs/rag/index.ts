import {
  Annotation,
  END,
  LangGraphRunnableConfig,
  MemorySaver,
  MessagesAnnotation,
  Send,
  START,
  StateGraph
} from "@langchain/langgraph";
import {MessageContent} from "@langchain/core/messages";
import {ToolNode} from "@langchain/langgraph/prebuilt";
import {llm} from "../../registry/registry";
import {z} from "zod";
import {getDefaultPromptConfig} from "./prompts";
import {researcherGraph} from "../researcher";
import {journeyPlannerTool} from "../../tools/journey_planner";
import {placesSearchTool} from "../../tools/places";

// State Definition
export const RetrievalGraphAnnotation = Annotation.Root({
  ...MessagesAnnotation.spec,
  /**
   * The research steps to be executed
   */
  steps: Annotation<string[] | undefined>,
  /**
   * The retrieved documents
   */
  documents: Annotation<Document[] | undefined>,
  /**
   * The original query from the user
   */
  query: Annotation<string | undefined>,
  /**
   * The final answer generated
   */
  answer: Annotation<MessageContent | undefined>,


  toolCalls: Annotation<string | undefined>,

  next: Annotation<string | undefined>
});

export type RetrievalGraphReturnType = Partial<
  typeof RetrievalGraphAnnotation.State
>;

const ALL_TOOLS_LIST = [journeyPlannerTool, placesSearchTool]

const toolNode = new ToolNode(ALL_TOOLS_LIST);

/**
 * Create a research plan
 */
export const createResearchPlan = async (
  state: typeof RetrievalGraphAnnotation.State,
  config: LangGraphRunnableConfig
): Promise<RetrievalGraphReturnType> => {
  const modelWithTool = llm.withStructuredOutput(
    z.object({
      steps: z.array(z.string())
    }),
    {name: "create_plan"}
  );


  const messages = [
    {role: "system", content: getDefaultPromptConfig().researchPlanSystemPrompt},
    ...state.messages
  ];

  const response = await modelWithTool.invoke(messages);

  const lastMessage = state.messages[state.messages.length - 1];
  return {
    steps: response.steps,
    documents: undefined, // Clear previous documents
    query: lastMessage?.content as string,
  };
};

/**
 * Execute research based on the plan
 */
export const conductResearch = async (
  state: typeof RetrievalGraphAnnotation.State
): Promise<RetrievalGraphReturnType> => {
  if (!state.steps || state.steps.length === 0) {
    throw new Error("No research steps found");
  }

  const result = await researcherGraph.invoke({
    question: state.steps[0],
    messages: []
  });

  return {
    documents: result.documents,
    steps: state.steps.slice(1)
  };
};

/**
 * Check if research is complete
 */
export const checkFinished = (state: typeof RetrievalGraphAnnotation.State): Send => {
  if (!state.steps) {
    return new Send("respond", state);
  }

  return new Send(
    state.steps.length > 0 ? "conduct_research" : "respond",
    state
  );
};

/**
 * Generate final response
 */
export const respond = async (
  state: typeof RetrievalGraphAnnotation.State,
  config: LangGraphRunnableConfig
): Promise<RetrievalGraphReturnType> => {
  const prompt = getDefaultPromptConfig().responseSystemPrompt.replace("{context}", "");

  const messages = [
    {role: "system", content: prompt},
    ...state.messages
  ];

  const lastMessage = messages[messages.length - 1];

  const response = await llm.bindTools(ALL_TOOLS_LIST).invoke(messages);

  console.log("response end", response)

  return {
    messages: [response],
    answer: response.content,
    toolCalls: JSON.stringify(response.tool_calls)
  };
};


const humanFeedback = (state: typeof RetrievalGraphAnnotation.State) => {
  console.log("--- humanFeedback ---");
  return state;
}


export const shouldContinue = (state: typeof MessagesAnnotation.State) => {
  const {messages} = state;
  const lastMessage = messages[messages.length - 1];

  if (lastMessage && "tool_calls" in lastMessage && Array.isArray(lastMessage.tool_calls) && lastMessage.tool_calls?.length) {
    console.log("--- Calling TOOL ---", lastMessage.tool_calls[0].name);
    return "tools";
  }

  return END
}

export const callModel = async (state: typeof MessagesAnnotation.State) => {
  console.log("--- Call Model ---")
  const messages = [
    {role: "system", content: getDefaultPromptConfig().responseSystemPrompt},
    ...state.messages
  ];

  const response = await llm.invoke(messages);

  return {messages: response};
}

// Build the graph
const builder = new StateGraph(RetrievalGraphAnnotation)
  // Add nodes
  .addNode("create_research_plan", createResearchPlan)
  .addNode("conduct_research", conductResearch)
  .addNode("tools", toolNode)
  .addNode("respond", respond)
  // Add edges
  .addEdge(START, "create_research_plan")
  .addEdge("create_research_plan", "conduct_research")
  // .addConditionalEdges(
  //   "conduct_research",
  //   checkFinished,
  //   ["conduct_research", "respond"]
  // )
  .addEdge("conduct_research", "respond")
  .addConditionalEdges("respond", shouldContinue, ["tools", END])
  .addEdge("tools", "respond")

const memory = new MemorySaver()

// Export the compiled graph
export const graphRag = builder.compile({
  // checkpointer: memory
});
