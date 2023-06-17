from enum import Enum
from typing import TypeVar, Protocol

from enums import MakeEnum, ModelEnum, EngineEnum, ColourEnum

Value = TypeVar("Value", bound=Enum)


class ConfigType(Protocol):
    def summary(self) -> str:
        ...


class BuilderInterface(Protocol):
    def choose_make(self, make: MakeEnum) -> 'BuilderInterface':
        ...

    def choose_model(self, model: ModelEnum) -> 'BuilderInterface':
        ...

    def choose_engine(self, engine: EngineEnum) -> 'BuilderInterface':
        ...

    def choose_colour(self, colour: ColourEnum) -> 'BuilderInterface':
        ...

    @property
    def product(self) -> ConfigType:
        ...


