import functools
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models.config import get_config


def session_manager_decorator(func):
    """Populates the session keyword argument if not provided."""

    @functools.wraps(func)
    def wrapper(arg, *args, session=None, **kwargs):
        if isinstance(session, Session) and not isinstance(session, MockSession):
            return func(arg, *args, session=session, **kwargs)
        with session_manager() as session:
            return func(arg, *args, session=session, **kwargs)

    return wrapper


@contextmanager
def session_manager():
    engine = get_engine()
    with Session(engine, expire_on_commit=False) as session:
        yield session
        session.commit()


def get_engine():
    config = get_config().db.model_dump()
    return create_engine(**config)


class MockSession(Session):
    def raise_error(self, *args, **kwargs):
        raise NotImplementedError("This is a mock class. Do not call this method.")

    update = add = commit = flush = query = get_one = raise_error
