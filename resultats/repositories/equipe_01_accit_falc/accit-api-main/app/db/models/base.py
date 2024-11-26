from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class UserFeedbackBase(MappedAsDataclass, DeclarativeBase):
    pass
