from lib.solutions.SUM.sum_solution import SumSolution
import pytest
import pydantic

from solutions.CHK.checkout_solution import CheckoutSolution


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
    assert CheckoutSolution().checkout(addend1, addend2) == expected


