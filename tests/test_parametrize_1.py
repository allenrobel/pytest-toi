import pytest

def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    return x * x

@pytest.mark.parametrize(
    "input, output",
    [
        (-10, 100),
        (0, 0),
        (10, 100),
        (10.3, pytest.approx(100.9, 0.1)),
    ],
)
def test_square(input, output):
    assert square(input) == output
