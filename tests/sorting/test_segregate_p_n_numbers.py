"""Tests for the segregate positive and negative numbers algorithm."""

from src.sorting.merge_sort.segregate_p_n_numbers import segregate_p_n_nums


def test_segregate_basic_mixed_numbers():
    """Tests segregation with basic mixed positive and negative numbers."""
    nums = [1, -2, 3, -4, 5]
    result = segregate_p_n_nums(nums)
    expected = [-2, -4, 1, 3, 5]
    assert result == expected


def test_segregate_maintains_relative_order():
    """Tests that relative order is maintained within positive and negative groups."""
    nums = [3, -1, 7, -5, 2, -8, 9]
    result = segregate_p_n_nums(nums)
    expected = [-1, -5, -8, 3, 7, 2, 9]
    assert result == expected


def test_segregate_empty_list():
    """Tests segregation with an empty list."""
    nums = []
    result = segregate_p_n_nums(nums)
    assert result == []


def test_segregate_single_positive():
    """Tests segregation with a single positive number."""
    nums = [5]
    result = segregate_p_n_nums(nums)
    assert result == [5]


def test_segregate_single_negative():
    """Tests segregation with a single negative number."""
    nums = [-5]
    result = segregate_p_n_nums(nums)
    assert result == [-5]


def test_segregate_all_positive():
    """Tests segregation with all positive numbers."""
    nums = [1, 3, 5, 7, 9]
    result = segregate_p_n_nums(nums)
    expected = [1, 3, 5, 7, 9]
    assert result == expected


def test_segregate_all_negative():
    """Tests segregation with all negative numbers."""
    nums = [-1, -3, -5, -7, -9]
    result = segregate_p_n_nums(nums)
    expected = [-1, -3, -5, -7, -9]
    assert result == expected


def test_segregate_with_zero():
    """Tests segregation with zero included."""
    nums = [1, 0, -2, 3, -4]
    result = segregate_p_n_nums(nums)
    expected = [0, -2, -4, 1, 3]
    assert result == expected


def test_segregate_multiple_zeros():
    """Tests segregation with multiple zeros."""
    nums = [1, 0, -2, 0, 3, -4, 0]
    result = segregate_p_n_nums(nums)
    expected = [0, -2, 0, -4, 0, 1, 3]
    assert result == expected


def test_segregate_does_not_modify_original():
    """Tests that segregate_p_n_nums does not modify the original list."""
    original = [1, -2, 3, -4, 5]
    original_copy = original.copy()
    
    result = segregate_p_n_nums(original)
    
    assert original == original_copy
    expected = [-2, -4, 1, 3, 5]
    assert result == expected


def test_segregate_large_numbers():
    """Tests segregation with large positive and negative numbers."""
    nums = [1000, -2000, 3000, -4000, 5000]
    result = segregate_p_n_nums(nums)
    expected = [-2000, -4000, 1000, 3000, 5000]
    assert result == expected


def test_segregate_duplicate_numbers():
    """Tests segregation with duplicate numbers."""
    nums = [2, -3, 2, -3, 1, -1]
    result = segregate_p_n_nums(nums)
    expected = [-3, -3, -1, 2, 2, 1]
    assert result == expected


def test_segregate_alternating_pattern():
    """Tests segregation with alternating positive and negative pattern."""
    nums = [1, -1, 2, -2, 3, -3, 4, -4]
    result = segregate_p_n_nums(nums)
    expected = [-1, -2, -3, -4, 1, 2, 3, 4]
    assert result == expected