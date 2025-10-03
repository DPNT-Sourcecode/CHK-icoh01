from lib.solutions.HLO.hello_solution import HelloSolution
import pytest
import pydantic


class NotQuiteAString:
    def __str__(self) -> str:
        return "foo"


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Matt", "Hello, Matt!"),
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
    ],
)
def test_hello_valid_inputs(name, expected):
    HelloSolution().hello(name)


@pytest.mark.parametrize(
    "name",
    [
        "",
        123,
        NotQuiteAString,
    ],
)
def test_hello_invalid_inputs(name):
    with pytest.raises(pydantic.ValidationError):
        HelloSolution().hello(name)
