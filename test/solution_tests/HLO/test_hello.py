from lib.solutions.HLO.hello_solution import HelloSolution

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
def test_hello_valid_inputs(name, expected):
    HelloSolution().hello(name)