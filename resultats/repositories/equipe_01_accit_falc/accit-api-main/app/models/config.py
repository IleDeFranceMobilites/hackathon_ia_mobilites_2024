from functools import cache
from typing import Type

from pydantic import BaseModel, ConfigDict
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
)


class ModelConfig(BaseModel):
    model_config = ConfigDict(extra="allow", protected_namespaces=tuple())
    model: str
    system_prompt: str


class LLMConfig(BaseModel):
    model_config = ConfigDict(extra="allow", protected_namespaces=tuple())
    model_class: str


class DBConfig(BaseModel):
    url: str
    echo: bool = False


class Config(BaseSettings):

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            YamlConfigSettingsSource(settings_cls, yaml_file="config.yaml"),
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )

    falceur: ModelConfig
    falc_scorer: ModelConfig
    db: DBConfig
    models: dict[str, LLMConfig]


@cache
def get_config():
    return Config()
