from typing import Any

from typing_extensions import reveal_type

from sqlalchemy.orm import DeclarativeBase, Mapped, InstrumentedAttribute


class Foo(DeclarativeBase):
    foobar: Mapped[str]


class Bar(DeclarativeBase):
    foobar: Mapped[str]


def foo(attribute: InstrumentedAttribute[Any]) -> None:
    pass


union: type[Foo | Bar] = Foo
foo(union.foobar)
