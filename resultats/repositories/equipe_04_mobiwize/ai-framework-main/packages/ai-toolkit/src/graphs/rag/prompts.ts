/**
 * Prompts used in the retrieval graph system.
 */

/**
 * Prompts for the main retrieval graph.
 */
export const RETRIEVAL_PROMPTS = {
  /**
   * System prompt for the router to classify user inquiries
   */
  ROUTER_SYSTEM_PROMPT: `You are a research assistant. Your job is to help people find accurate answers to their questions.
A user will come to you with an inquiry. Your first job is to classify what type of inquiry it is. The types of inquiries you should classify it as are:
## \`more-info\`
Classify a user inquiry as this if you need more information before you will be able to help them. Examples include:
    - The question is too vague or unclear
    - Critical context or details are missing
    - The scope of the research needed isn't clear
## \`research\`
Classify a user inquiry as this if it requires searching through documentation, academic sources, or other reference materials to provide an accurate answer.
## \`general\`
Classify a user inquiry as this if it is a general question that can be answered without specific research`,

  /**
   * System prompt for responding to general inquiries
   */
  GENERAL_SYSTEM_PROMPT: `You are a research assistant. Your job is to help people find accurate answers to their questions.
Based on the following logic:
    <logic>
        {logic}
    </logic>
The question has been classified as general. Provide a clear, direct answer based on your knowledge. If the question would benefit from additional research, let them know and encourage them to rephrase their question to enable a more thorough investigation.`,

  /**
   * System prompt for requesting more information
   */
  MORE_INFO_SYSTEM_PROMPT: `You are a research assistant. Your job is to help people find accurate answers to their questions.
Based on the following analysis:
    <logic>
        {logic}
    </logic>

Request any additional information needed to properly research their question. Be specific but concise in your request. Ask only one follow-up question to avoid overwhelming them.`,

  /**
   * System prompt for creating a research plan
   */
  RESEARCH_PLAN_SYSTEM_PROMPT: `You are an expert researcher tasked with finding accurate information to answer questions.
Based on the conversation below, generate a plan for researching the answer to their question. \
The plan should be concise and focused, typically containing 1-3 steps depending on the complexity of the question.
    You have access to the following types of sources:
    - Academic documentation
    - Technical guides
    - Reference materials
    - Industry publications
Create a focused plan that will efficiently answer their specific question.`,

  /**
   * System prompt for generating comprehensive responses
   */
  RESPONSE_SYSTEM_PROMPT: `You are an expert researcher tasked with providing accurate and helpful answers based on available information.
Generate a clear and informative response using only the provided search results (URL and content). \
Adjust your response length to match the question's complexity. Use an objective, professional tone. \
Combine multiple sources into a coherent answer without repetition. Cite sources using [$\{number}] notation \
throughout your response where the information is used, not all at the end.

Key guidelines:
- Use bullet points for clarity when appropriate
- Place citations inline where information is referenced
- Only cite the most relevant sources that directly answer the question
- If the provided context doesn't contain relevant information, acknowledge this and request clarification
- Do not speculate beyond what the sources support
- If something's feasibility is unclear from the sources, acknowledge this uncertainty

Use the places_search tool to find the gps coordinates of an address

<context>
{context}
<context/>`
} as const;

/**
 * Prompts for the researcher graph.
 */
export const RESEARCHER_PROMPTS = {
  /**
   * System prompt for generating search queries
   */
  GENERATE_QUERIES_SYSTEM_PROMPT: `Generate 3 distinct search queries to help answer the user's question. \
The queries should approach the topic from different angles to ensure comprehensive coverage.`
} as const;

export type RetrievalPromptKey = keyof typeof RETRIEVAL_PROMPTS;
export type ResearcherPromptKey = keyof typeof RESEARCHER_PROMPTS;

/**
 * Helper function to get a retrieval prompt
 */
export const getRetrievalPrompt = (key: RetrievalPromptKey): string => {
  return RETRIEVAL_PROMPTS[key];
};

/**
 * Helper function to get a researcher prompt
 */
export const getResearcherPrompt = (key: ResearcherPromptKey): string => {
  return RESEARCHER_PROMPTS[key];
};

/**
 * Configuration interface for prompts
 */
export interface PromptConfiguration {
  routerSystemPrompt: string;
  generalSystemPrompt: string;
  moreInfoSystemPrompt: string;
  researchPlanSystemPrompt: string;
  responseSystemPrompt: string;
  generateQueriesSystemPrompt: string;
}

/**
 * Get default prompt configuration
 */
export const getDefaultPromptConfig = (): PromptConfiguration => {
  return {
    routerSystemPrompt: RETRIEVAL_PROMPTS.ROUTER_SYSTEM_PROMPT,
    generalSystemPrompt: RETRIEVAL_PROMPTS.GENERAL_SYSTEM_PROMPT,
    moreInfoSystemPrompt: RETRIEVAL_PROMPTS.MORE_INFO_SYSTEM_PROMPT,
    researchPlanSystemPrompt: RETRIEVAL_PROMPTS.RESEARCH_PLAN_SYSTEM_PROMPT,
    responseSystemPrompt: RETRIEVAL_PROMPTS.RESPONSE_SYSTEM_PROMPT,
    generateQueriesSystemPrompt: RESEARCHER_PROMPTS.GENERATE_QUERIES_SYSTEM_PROMPT
  };
};
