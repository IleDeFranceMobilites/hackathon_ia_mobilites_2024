from datetime import datetime
import os

from langchain.agents import AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI

from sources.agent.tools.get_itineraire import get_itineraire
from sources.agent.tools.get_info_trafic import get_info_trafic


from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser

API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION')
AZURE_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
API_KEY = os.getenv('AZURE_OPENAI_API_KEY')

MEMORY_KEY = "chat_history"
CHAT_HISTORY = []

TOOLS = [get_itineraire, get_info_trafic]

azure_open_ai_parameters = {
    "api_version": API_VERSION,
    "azure_endpoint": AZURE_ENDPOINT,
    "api_key": API_KEY
}

llm = AzureChatOpenAI(
    **azure_open_ai_parameters,
    model=os.getenv('AZURE_OPENAI_MODELS'),
    temperature=0.2,
)

llm_with_tools = llm.bind_tools(TOOLS)

custom_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            f"""
            Vous êtes un assistant spécialisé pour aider les usagers de l'Île-de-France à trouver leur itinéraire dans les transports en commun.

            Consignes :
            Utilisez un langage simple et naturel, car le texte sera lu à voix haute.
            Nous sommes le {datetime.now().strftime("%Y-%m-%d")}.
            Il est {datetime.now().strftime("%H:%M:%S")}.
            Si l'utilisateur n'en fournit pas, considère que c'est la date et heure de départ.
            Si le point de départ n’est pas précisé :
            Utilisez la géolocalisation de l’usager si elle est disponible.
            Sinon, invitez-le à l’activer ou à préciser son départ. Ne faites pas d’hypothèses.
            Mais utilisez le point de départ s'il est précisé.

            Si la requête semble incomplete demandez plus de précisions.

            Répondez en 4 lignes maximum.
            Fournissez la réponse en indiquant l'origine et la destination, la date de départ et la date d'arrivée et les étapes principales, comme suit :
            Exemple :
            En partant 56 Rue de Bagnolet au 34 avenue de l'Opéra aujourd'hui à 14h, vous arriverez à 14h38. Marchez 6 minutes jusqu'à la station Alexandre Dumas, puis prenez la ligne 2 pendant 3 minutes direction Porte Dauphine jusqu'à Père Lachaise. Changez pour la ligne 3 direction Pont de Levallois pendant 11 minutes et descendez à Opéra.
            """,
        ),
        ("system", "User location: {user_location}"),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = (
    {
        "input": lambda x: x["input"],
        "user_location": lambda x: x["user_location"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
        "chat_history": lambda x: x["chat_history"],
    }
    | custom_prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)


agent_executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=True)


def invoke_agent(message: str, location: str) -> str:

    result = agent_executor.invoke({"input": message, "user_location": location, "chat_history": CHAT_HISTORY})

    CHAT_HISTORY.extend(
        [
            HumanMessage(content=message),
            AIMessage(content=result["output"]),
        ]
    )

    return result["output"]


if __name__ == "__main__":
    invoke_agent(
        message=("Je veux aller de la basilique Montmartre a la gare Montparnasse"),
        location=None
    )
