from config import Config
from kata_typing import Value, BuilderInterface
from typing import Sequence

from enums import MakeEnum, ModelEnum, EngineEnum, ColourEnum


class CarBuilder(BuilderInterface):
    Choices = dict[Value, Sequence[Value]]
    permissible_model = {
        MakeEnum.JAGUAR: [ModelEnum.F_TYPE]
    }
    permissible_engines = {
        ModelEnum.F_TYPE: [EngineEnum.V8_4_0]
    }

    def __init__(self):
        self._config = Config()

    def reset(self):
        self._config = Config()

    def choose_make(self, make: MakeEnum) -> 'BuilderInterface':
        self._config.add(make, "make")
        self._config.permissible_options = self.permissible_model.get(make)
        return self

    def choose_model(self, model: ModelEnum) -> 'BuilderInterface':
        self._config.add(model, "model")
        self._config.permissible_options = self.permissible_engines.get(model)
        return self

    def choose_engine(self, engine: EngineEnum) -> 'BuilderInterface':
        self._config.add(engine, "engine")
        self._config.permissible_options = None
        return self

    def choose_colour(self, colour: ColourEnum) -> 'BuilderInterface':
        self._config.add(colour, "colour")
        self._config.permissible_options = None
        return self

    @property
    def product(self) -> Config:
        return self._config


