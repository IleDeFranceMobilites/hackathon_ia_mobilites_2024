import {type ElasticClientArgs, ElasticVectorSearch,} from "@langchain/community/vectorstores/elasticsearch";
import {AzureOpenAIEmbeddings} from "@langchain/openai";
import {Client, type ClientOptions} from "@elastic/elasticsearch";
import * as process from "node:process";

export const embeddings = new AzureOpenAIEmbeddings({
  azureOpenAIApiDeploymentName: "text-embedding-3-large",
  azureOpenAIApiInstanceName: "dlb-team04-prd-oai01",
  azureOpenAIApiKey: process.env.AZURE_OPENAI_API_KEY,
  azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_VERSION,
  model: "text-embedding-3-large",
});


const config: ClientOptions = {
  node: process.env.ELASTIC_URL ?? "https://127.0.0.1:9200",
};

config.auth = {
  apiKey: process.env.ELASTIC_API_KEY as string,
};

const clientArgs: ElasticClientArgs = {
  client: new Client(config),
  indexName: "idfm-eq4"
};

export const vectorStore = new ElasticVectorSearch(embeddings, clientArgs);
