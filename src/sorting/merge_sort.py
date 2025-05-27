"""Module for merge sort implementation."""


def merge_sort(nums: list) -> list:
    """
    Sorts a list of numbers in ascending order using the merge sort algorithm.

    Merge sort is a divide-and-conquer algorithm that divides the input array into two halves,
    recursively sorts them, and then merges the sorted halves.

    Args:
        nums (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.
    """
    # Create a copy of the input list to avoid modifying the original
    if not nums:
        return []

    if len(nums) == 1:
        return nums

    # make a copy to avoid modifying the original list
    nums_copy = nums.copy()

    # call the helper function to perform the actual sorting
    _merge_sort_helper(nums_copy, 0, len(nums_copy) - 1)

    return nums_copy


def _merge_sort_helper(nums: list, start: int, end: int) -> None:
    """
    Helper function that implements the recursive merge sort algorithm.

    Args:
        nums (list): The list to be sorted.
        start (int): The starting index of the subarray.
        end (int): The ending index of the subarray.

    Returns:
        None: The list is modified in-place.
    """
    if start >= end:
        return

    # find the middle point to divide the array into two halves
    mid = (start + end) // 2

    # recursively sort the first and second halves
    _merge_sort_helper(nums, start, mid)
    _merge_sort_helper(nums, mid + 1, end)

    # merge the sorted halves
    _merge(nums, start, mid, end)


def _merge(nums: list, start: int, mid: int, end: int) -> None:
    """
    Merges two sorted subarrays into a single sorted subarray.

    Args:
        nums (list): The list containing the subarrays to be merged.
        start (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray.
        end (int): The ending index of the second subarray.

    Returns:
        None: The list is modified in-place.
    """
    # create temporary arrays for the two halves
    left_arr = nums[start : mid + 1]
    right_arr = nums[mid + 1 : end + 1]

    # initial indices for a left array, right array, and merged array
    l, r, k = 0, 0, start

    # merge the two arrays back into nums[start...end]
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            nums[k] = left_arr[l]
            l += 1
        else:
            nums[k] = right_arr[r]
            r += 1
        k += 1

    # copy the remaining elements of left_arr, if any
    while l < len(left_arr):
        nums[k] = left_arr[l]
        l += 1
        k += 1

    # copy the remaining elements of right_arr, if any
    while r < len(right_arr):
        nums[k] = right_arr[r]
        r += 1
        k += 1
