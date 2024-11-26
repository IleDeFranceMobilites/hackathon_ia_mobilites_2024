from openai import AzureOpenAI
from llm.keys import OPENAI_ENDPOINT, MODEL_NAME, AZURE_OPENAI_KEY
from ecologits import EcoLogits

EcoLogits.init()

# Configuration du LLM
class LLMConfiguration:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=AZURE_OPENAI_KEY,
            api_version="2024-03-01-preview",
            azure_endpoint=OPENAI_ENDPOINT
        )
        
        self.default_params = {
            "model": MODEL_NAME,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "max_tokens": None
        }
        
    def invoke(self, prompt):
        """
        Méthode pour exécuter une requête au LLM
        
        Args:
            prompt (str): Le prompt à envoyer au LLM
            
        Returns:
            dict: La réponse du LLM au format JSON
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            **self.default_params
        )
        return response
