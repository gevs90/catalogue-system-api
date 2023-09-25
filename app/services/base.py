from typing import (
    Any,
    List,
    Sequence
)
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Executable

from app.models.base import SQLModel


class SessionMixin:
    """Provides instance of database session."""

    def __init__(self, session: Session) -> None:
        self.session = session


class BaseService(SessionMixin):
    """Base class for application services."""


class BaseDataManager(SessionMixin):
    """Base data manager class responsible for operations over database."""

    def add_one(self, model: Any, recover: bool = False) -> None | Any:
        self.session.add(model)
        self.session.commit()
        if recover:
            self.session.refresh(model)
            return model

    def update_one(self, model: Any, recover: bool = False) -> None | Any:
        self.session.commit()
        if recover:
            self.session.refresh(model)
            return model

    def destroy_one(self, model: Any) -> bool:
        self.session.delete(model)
        self.session.commit()
        return True

    def add_all(self, models: Sequence[Any]) -> None:
        self.session.add_all(models)

    def get_one(self, select_stmt: Executable) -> Any:
        return self.session.scalar(select_stmt)

    def get_all(self, select_stmt: Executable) -> List[Any]:
        return list(self.session.scalars(select_stmt).all())
