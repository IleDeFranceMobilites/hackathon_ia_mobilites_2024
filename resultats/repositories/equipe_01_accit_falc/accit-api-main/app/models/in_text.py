from pydantic import BaseModel


class NormalText(BaseModel):
    text: str


class FalcText(BaseModel):
    falc_text: str
