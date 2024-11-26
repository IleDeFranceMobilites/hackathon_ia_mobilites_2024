import {AzureChatOpenAI} from "@langchain/openai";

export const llm = new AzureChatOpenAI({
  azureOpenAIEndpoint: process.env.AZURE_OPENAI_ENDPOINT,
  azureOpenAIApiKey: process.env.AZURE_OPENAI_API_KEY,
  azureOpenAIApiDeploymentName: process.env.AZURE_OPENAI_MODELS,
  azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_VERSION,
  model: process.env.AZURE_OPENAI_MODELS,
  temperature: 0.1,
});
