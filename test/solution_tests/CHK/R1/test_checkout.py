import pytest

from solutions.CHK.checkout_solution import CheckoutSolution


class MockIntType:
    def __int__(self):
        return 1


@pytest.mark.parametrize(
    "skus,expected",
    [("ABCD", 115), ("ABCDABBD", 225)],
)
def test_valid_inputs(skus, expected):
    assert CheckoutSolution().checkout(skus) == expected


