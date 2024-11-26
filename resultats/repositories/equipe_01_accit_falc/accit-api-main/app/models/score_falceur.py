from pydantic import BaseModel


class FalcScore(BaseModel):
    good: list[str]
    bad: list[str]
    improve: list[str]
    score: float
