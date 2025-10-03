import pytest

from solutions.CHK.checkout_solution import CheckoutSolution


@pytest.mark.parametrize(
    "skus,expected",
    [
        ("AAA", 130),
        ("AAAAA", 200),
        ("AAAAAA", 250),
        ("AAAAAAAA", 330),
        ("AAAAAAAAAA", 400),
        ("BB", 45),
        ("EE", 80),
        ("EEB", 80),
        ("EEBB", 110),
        ("EEBBB", 125),
        ("EAEBCBBAA", 125+130+20),
        ("AAABB", 175),
        ("ABCDABCD", 215),
        ("ABCD", 115),
        ("ABCDABBD", 225),
        ("AABABADABBCAADBABAAA", 675),
    ],
)
def test_valid_inputs(skus, expected):
    assert CheckoutSolution().checkout(skus) == expected


@pytest.mark.parametrize(
    "skus",
    [
        "ABCDZ",
        "abcd",
        5,
    ],
)
def test_invalid_inputs(skus):
    assert CheckoutSolution().checkout(skus) == -1
