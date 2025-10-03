from lib.solutions.SUM.sum_solution import SumSolution
import pytest
import pydantic

from solutions.CHK.checkout_solution import CheckoutSolution


class MockIntType:
    def __int__(self):
        return 1


@pytest.mark.parametrize(
    "skus,expected",
    [
        ("ABCD", 115)
    ],
)
def test_valid_inputs(addend1, addend2, expected):
    assert CheckoutSolution().checkout(addend1, addend2) == expected

