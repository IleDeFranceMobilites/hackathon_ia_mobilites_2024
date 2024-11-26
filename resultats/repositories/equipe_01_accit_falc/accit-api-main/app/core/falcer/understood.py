from app.db.models.user_feedback import FalcUserFeedBack
from app.models.falc_understood import FalcUnderstood


def store_falc_feedback(data: FalcUnderstood) -> None:
    user_feedback = FalcUserFeedBack(
        non_falc_text=data.text, falc_text=data.falc_text, understood=data.understood
    )
    user_feedback.add()


def get_all_falc_feedback() -> list[FalcUserFeedBack]:
    return FalcUserFeedBack.get_all()
