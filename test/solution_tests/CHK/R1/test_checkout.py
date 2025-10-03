import pytest

from solutions.CHK.checkout_solution import CheckoutSolution


class MockIntType:
    def __int__(self):
        return 1


@pytest.mark.parametrize(
    "skus,expected",
    [("ABCD", 115), ("ABCDABBD", 225), ("AABABADABBCAADBABAAA", 675)],
)
def test_valid_inputs(skus, expected):
    assert CheckoutSolution().checkout(skus) == expected


@pytest.mark.parametrize(
    "skus",
    [
        "ABCDZ",
        5,
        "abcd",
    ],
)
def test_invalid_inputs(skus):
    with pytest.raises(ValueError):
        assert CheckoutSolution().checkout(skus)


