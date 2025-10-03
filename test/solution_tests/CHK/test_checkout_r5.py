import pytest

from solutions.CHK.checkout_solution import CheckoutSolution


@pytest.mark.parametrize(
    "skus,expected",
    [
        # ("AAA", 130),
        # ("AAAAA", 200),
        # ("AAAAAA", 250),
        # ("AAAAAAAA", 330),
        # ("AAAAAAAAAA", 400),
        # ("BB", 45),
        # ("EE", 80),
        # ("EEB", 80),
        # ("EEBB", 110),
        # ("EEBBB", 125),
        # ("FF", 20),
        # ("FFF", 20),
        # ("FFFFFF", 40),
        # ("EAEBCBBAA", 275),
        # ("AAABB", 175),
        # ("ABCDABCD", 215),
        # ("ABCD", 115),
        # ("ABCDABBD", 225),
        ("ABCDABBDSTX", -1),
        ("ABSCSDSABBD", -1),
        ("ABSCSDSAXBXBDXSYTZ", -1),
        # ("AABABADABBCAADBABAAA", 635),
        # ("AABAFBAFDABBFFCAADFFFBABAAA", 685),
    ],
)
def test_valid_inputs(skus, expected):
    assert CheckoutSolution().checkout(skus) == expected


@pytest.mark.parametrize(
    "skus",
    [
        "ABCD~",
        "abcd",
        5,
    ],
)
def test_invalid_inputs(skus):
    assert CheckoutSolution().checkout(skus) == -1


