from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from app.core.models import get_model
from app.db.models.user_feedback import FalcUserFeedBack
from app.models.config import get_config


def falcate_a_text(model: BaseChatModel, system_prompt: str, user_prompt: str) -> str:
    custom_rag_prompt = PromptTemplate.from_template(system_prompt)

    rag_chain = (
        {"question": RunnablePassthrough()}
        | custom_rag_prompt
        | model
        | StrOutputParser()
    )

    return rag_chain.invoke(user_prompt)


def falcate(text_to_falcate: str) -> str:
    config = get_config()

    model_to_use = config.falceur.model
    model_config = config.models[model_to_use]

    model = get_model(model_to_use, model_config)

    return falcate_a_text(model, config.falceur.system_prompt, text_to_falcate)


def score_a_text(model: BaseChatModel, system_prompt: str, user_prompt: str) -> dict:
    custom_rag_prompt = PromptTemplate.from_template(system_prompt)

    rag_chain = (
        {"text": RunnablePassthrough()} | custom_rag_prompt | model | JsonOutputParser()
    )

    return rag_chain.invoke(user_prompt)


def falc_text_score(text_to_score: str) -> dict:
    config = get_config()

    model_to_use = config.falc_scorer.model
    model_config = config.models[model_to_use]

    model = get_model(model_to_use, model_config)

    user_feedbacks = parse_user_feedback(FalcUserFeedBack.get_all())

    system_prompt = config.falc_scorer.system_prompt
    system_prompt_with_feedback = f"{system_prompt}\n\nVoici des examples de textes précédemment générés :\n{user_feedbacks}"

    return score_a_text(model, system_prompt_with_feedback, text_to_score)


def parse_user_feedback(feedbacks: list[FalcUserFeedBack]) -> str:
    for feedback in feedbacks:
        if feedback.understood:
            return (
                f"Le texte simplifié suivant a été compris : '{feedback.falc_text}'. "
                f"Le texte original était : '{feedback.non_falc_text}'"
            )
        else:
            return (
                f"Le texte simplifié suivant n'a PAS été compris : '{feedback.falc_text}'. "
                f"Il faudrait que {feedback.non_falc_text} suivent mieux les règles énoncées."
            )
