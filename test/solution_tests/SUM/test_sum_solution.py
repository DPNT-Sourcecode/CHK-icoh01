from lib.solutions.SUM.sum_solution import SumSolution
import pytest
import pydantic

class MockIntType:
    def __int__(self):
        return 1

@pytest.mark.parametrize(
    "addend1,addend2,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (100, 100, 200),  # assuming 0-100 is inclusive
        (35, 66, 101),
        (55, 92, 147),
    ],
)
def test_valid_inputs(addend1, addend2, expected):
    assert SumSolution().compute(addend1, addend2) == expected


@pytest.mark.parametrize(
    "addend1,addend2",
    [
        (-5, 10),
        (10, -5),
        (-5, -5),
    ],
)
def test_negative_inputs(addend1, addend2):
    with pytest.raises(pydantic.ValidationError):
        assert SumSolution().compute(addend1, addend2)


@pytest.mark.parametrize(
    "addend1,addend2",
    [
        ("23", 10),
        (19, "45"),
        ("3", "12"),
        (1, True),
        (-10, "yes"),
        (pydantic.BaseModel, 4),
        (MockIntType(), 5),  # assuming we don't want to support type coercion, only want literal `int` types
    ],
)
def test_invalid_input_types(addend1, addend2):
    with pytest.raises(pydantic.ValidationError):
        assert SumSolution().compute(addend1, addend2)