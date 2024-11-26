from sqlalchemy.orm import Mapped, Session, mapped_column
from typing_extensions import Self

from ..utils import MockSession, session_manager_decorator
from .base import UserFeedbackBase


class FalcUserFeedBack(UserFeedbackBase):
    """supercharge celery task table."""

    __tablename__ = "falc_user_feedback"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    non_falc_text: Mapped[str]
    falc_text: Mapped[str]
    understood: Mapped[bool]

    @session_manager_decorator
    def add(self, *, session: Session = MockSession()) -> Self:
        session.add(self)
        session.flush()
        return self

    @classmethod
    @session_manager_decorator
    def get_all(cls, *, session: Session = MockSession()) -> Self:
        return session.query(cls).all()
