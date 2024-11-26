import importlib
import os

from app.models.config import LLMConfig


def get_model(model_name: str, params: LLMConfig):
    model_package, module_name = params.model_class.rsplit(".", 1)

    module = importlib.import_module(model_package)
    module = getattr(module, module_name)

    fill_secrets_from_env(model_name, params)

    return module(**params.model_dump(exclude=["model_class"]))


def fill_secrets_from_env(model_name: str, params: LLMConfig):
    for key, value in params.model_dump().items():
        if value == "SECRET":
            setattr(params, key, os.getenv(f"{model_name.upper()}_{key.upper()}"))
