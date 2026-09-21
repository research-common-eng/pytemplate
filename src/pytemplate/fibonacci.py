"""A small example of recursion."""


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, starting with F(0) = 0 and F(1) = 1.

    Raises ValueError for negative indices. This simple recursive implementation
    repeats work and is intended for small inputs.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
