from pydantic import BaseModel


class FalcUnderstood(BaseModel):
    text: str
    falc_text: str
    understood: bool


class FalcFeedBack(BaseModel):
    non_falc_text: str
    falc_text: str
    understood: bool
