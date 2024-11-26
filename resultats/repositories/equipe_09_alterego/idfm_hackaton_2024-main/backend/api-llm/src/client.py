import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from pathlib import Path


class Client:
    def __init__(self):
        path_secrets = os.getcwd()+"/secrets.env"
        load_dotenv(dotenv_path=Path(path_secrets).resolve())
        self.openAiKey = os.getenv("OPENAI_API_KEY")
        self.end_point = os.getenv("OPENAI_AZURE_ENDPOINT")
        self.api_version = os.getenv("API_VERSION")

    def get_client(self):
        client = AzureOpenAI(
            azure_endpoint=self.end_point,
            api_key=self.openAiKey,
            api_version=self.api_version
        )
        return client