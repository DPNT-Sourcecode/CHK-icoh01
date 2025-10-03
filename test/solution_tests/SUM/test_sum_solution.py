from lib.solutions.SUM.sum_solution import SumSolution
import pytest


@pytest.mark.parametrize("addend1,addend2,expected", [(1, 2, 3)])
def test_sum_valid_inputs(addend1, addend2, expected):
    assert SumSolution().compute(1, 2) == 3

