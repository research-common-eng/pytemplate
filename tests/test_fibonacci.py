"""Tests for the example Fibonacci function."""

import pytest

from pytemplate.fibonacci import fibonacci


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (10, 55)],
)
def test_fibonacci(n: int, expected: int) -> None:
    assert fibonacci(n) == expected


@pytest.mark.parametrize("n", [-1, -10])
def test_fibonacci_rejects_negative_indices(n: int) -> None:
    with pytest.raises(ValueError, match="n must be non-negative"):
        fibonacci(n)
