import openai
import os
from openai import AzureOpenAI
from client import Client
from nlu import Nlu


class Chatbot:
    def __init__(self, history):
        self.client = Client()
        self.client = self.client.get_client()
        self.model = 'gpt-4o-mini'

    def ask_gpt(self, conversation_history, message):
        nlu = Nlu()
        intention = nlu.get_intentions_entites(message)
        if (intention == "RELATED_IDFM"){
            retrun "Comment je peux vous aider"
        }
        else{
            retrun ""
        }