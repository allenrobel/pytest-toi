import pytest
from contextlib import contextmanager
from modules.square import square
# def square(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError("x must be numeric")
#     return x * x

@contextmanager
def does_not_raise():
    """
    A context manager that does not raise an exception.
    """
    yield

@pytest.mark.parametrize(
    "input, output, context",
    [
        (-10, 100, does_not_raise()),
        (0, 0, does_not_raise()),
        (10, 100, does_not_raise()),
        (10.3, pytest.approx(100.9, 0.1), does_not_raise()),
        ("b", None, pytest.raises(TypeError, match="x must be numeric")),
    ],
)
def test_square_better(input, output, context):
    with context:
        assert square(input) == output
