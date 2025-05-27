"""Module for recursion and visualization for it."""


def factorial(num: int) -> int:
    """
    Calculate factorial of a given number.
    Args:
        num (int): Number to calculate factorial for.
    Returns:
        int: Factorial of the given number.
    """
    if num == 0:
        return 1
    return num * factorial(num - 1)
