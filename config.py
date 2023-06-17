import dataclasses
from enum import Enum
from typing import Optional, Sequence

from enums import EngineEnum, MakeEnum, ModelEnum, ColourEnum
from kata_typing import Value


@dataclasses.dataclass
class Config:
    make: Optional[Value] = None
    model: Optional[Value] = None
    engine: Optional[Value] = None
    colour: Optional[Value] = None
    permissible_options: Optional[Sequence[Enum]] = None

    def add(self, v: Value, as_attr: str):
        if not self.permissible_options or v in self.permissible_options:
            self.__setattr__(as_attr, v)
        else:
            raise ValueError

    def summary(self):
        enum_str_mapping: dict[Value, str] = {
            EngineEnum.V8_4_0: "V8 4.0",
            MakeEnum.JAGUAR: "Jaguar",
            ModelEnum.F_TYPE: "F-Type",
            ColourEnum.BRITISH_RACING_GREEN: "BRG"
        }
        make, model, engine, colour = tuple(map(enum_str_mapping.get, (self.make, self.model, self.engine, self.colour)))
        return f"{make} {model} {engine} {colour}"


