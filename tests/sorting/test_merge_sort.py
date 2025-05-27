"""Tests for the merge sort algorithm."""

from src.sorting.merge_sort import merge_sort


def test_merge_sort():
    """Tests the merge sort function with various test cases."""
    nums = [3, 2, 1, 5, 4]
    assert merge_sort(nums) == [1, 2, 3, 4, 5]

    nums = [1, 2, 3, 4, 5]
    assert merge_sort(nums) == [1, 2, 3, 4, 5]

    nums = [5, 4, 3, 2, 1]
    assert merge_sort(nums) == [1, 2, 3, 4, 5]

    nums = []
    assert not merge_sort(nums)

    nums = [42]
    assert merge_sort(nums) == [42]

    nums = [3, -1, 0, 2, -2, 1]
    assert merge_sort(nums) == [-2, -1, 0, 1, 2, 3]


def test_merge_sort_does_not_modify_original():
    """Tests that merge_sort does not modify the original list."""
    original = [3, 2, 1, 5, 4]
    original_copy = original.copy()

    sorted_list = merge_sort(original)

    # Check that the original list is unchanged
    assert original == original_copy
    # Check that the returned list is sorted
    assert sorted_list == [1, 2, 3, 4, 5]
