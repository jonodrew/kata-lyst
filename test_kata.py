import pytest

from car_builder import CarBuilder
from enums import MakeEnum, ModelEnum, EngineEnum, ColourEnum


@pytest.mark.parametrize(
    ["make", "model", "engine", "colour", "summary"], [
        ("Jaguar", "F-Type", "4 litre V8", "British Racing Green", "Jaguar F-Type V8 4.0 BRG")
    ]
)
def test_user_journey(make, model, engine, colour, summary):
    """

    Bill starts to configure a new "Jaguar"
    Bill chooses to configure the new "F-Type"
    Bill selects the "4 litre V8" engine
    Bill selects the "British Racing Green" colour for his "F-Type"
    Bill sees the configuration summary "Jaguar F-Type V8 4.0 BRG"

    :return:
    """
    car_builder = CarBuilder().choose_make(MakeEnum.JAGUAR).choose_model(ModelEnum.F_TYPE).choose_engine(EngineEnum.V8_4_0).choose_colour(ColourEnum.BRITISH_RACING_GREEN).product
    assert car_builder.summary() == "Jaguar F-Type V8 4.0 BRG"

