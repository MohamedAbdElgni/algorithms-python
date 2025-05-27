"""Module for testing recursion."""

from src.declarative.recursion import factorial


def test_factorial():
    """Test factorial."""
    assert factorial(5) == 120
