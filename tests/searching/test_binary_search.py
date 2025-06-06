"""Tests for binary search algorithm."""

from src.searching.binary_search import binary_search


def test_binary_search():
    """Tests the binary search function with various test cases."""
    # Test finding elements at different positions
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 5) == 4

    # Test element not in array
    assert binary_search(arr, 6) == -1
    assert binary_search(arr, 0) == -1

    # Test empty array
    assert binary_search([], 1) == -1

    # Test single element array
    assert binary_search([42], 42) == 0
    assert binary_search([42], 41) == -1

    # Test array with negative numbers
    arr = [-5, -2, 0, 3, 7, 9]
    assert binary_search(arr, -5) == 0
    assert binary_search(arr, 0) == 2
    assert binary_search(arr, 9) == 5
    assert binary_search(arr, -3) == -1

    # Test array with duplicate elements
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    # Binary search typically returns the index of any matching element (not necessarily the first)
    result = binary_search(arr, 3)
    assert arr[result] == 3

    # Test large array
    arr = list(range(100))
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 50) == 50
    assert binary_search(arr, 99) == 99
    assert binary_search(arr, 100) == -1
