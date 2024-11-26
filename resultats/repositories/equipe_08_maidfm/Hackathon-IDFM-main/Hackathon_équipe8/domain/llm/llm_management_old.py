from langchain_openai import AzureChatOpenAI
from llm.keys import OPENAI_ENDPOINT, MODEL_NAME, AZURE_OPENAI_KEY

# Configuration du LLM
class LLMConfiguration:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            model=MODEL_NAME,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=AZURE_OPENAI_KEY,
            azure_endpoint=OPENAI_ENDPOINT,
            api_version="2024-03-01-preview"
        )
        self.llm.bind(response_format={"type": "json_object"})
