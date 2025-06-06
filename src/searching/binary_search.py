"""Module for binary search."""


def binary_search(arr: list, k: int) -> int:
    """
    Searches for a number in a sorted list using the binary search algorithm.
    Args:
        arr (list): A sorted list of numbers to search in.
        k (int): The number to be searched.
    Returns:
        int: The index of the number if found, -1 otherwise.
    """
    l, h = 0, len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        if k == arr[mid]:
            return mid

        if k > arr[mid]:
            l = mid + 1
        else:
            h = mid - 1

    return -1
