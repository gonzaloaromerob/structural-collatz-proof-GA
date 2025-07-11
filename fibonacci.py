# fibonacci.py

"""Simple module to generate Fibonacci series."""

from typing import List


def fibonacci(n: int) -> List[int]:
    """Return a list containing the Fibonacci series up to n terms."""
    if n <= 0:
        return []
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]


if __name__ == "__main__":
    import sys
    terms = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(fibonacci(terms))
