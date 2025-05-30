"""Module for insertion sort implementation."""


def insertion_sort(nums: list):
    """
    Sorts a list of numbers in ascending order using the insertion sort algorithm.
    Args:
        nums (list): A list of numbers to be sorted.
    Returns:
        list: The sorted list of numbers.
    """
    # Start from the second element as the first element is already sorted
    current_index = 1
    while current_index < len(nums):
        # The element to be positioned in the sorted part of the array
        current_value = nums[current_index]
        # The last index of the sorted part of the array
        sorted_index = current_index - 1
        while sorted_index >= 0:
            if nums[sorted_index] > current_value:
                nums[sorted_index + 1] = nums[sorted_index]
                sorted_index -= 1
            else:
                break
        nums[sorted_index + 1] = current_value
        current_index += 1

    return nums
