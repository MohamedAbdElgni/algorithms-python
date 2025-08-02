"""
Segregate positive and negative numbers  with merge sort
"""

from src.utils.debug_utils import debug_print


def segregate_p_n_nums(nums:list):
    """
    Segregates an array of numbers into positive and negative numbers while maintaining their
    original relative order.

    Args:
        nums (list): A list of integers to be segregated.

    Returns:
        list: A new list with negative elements followed by positive elements, retaining their
        original relative order from the input list.
    """
    if not nums:
        return []

    if len(nums) == 1:
        return nums

    nums_copy = nums.copy()
    debug_print(f"Starting segregation with array: {nums_copy}")
    debug_print("=" * 50)

    _segregate_p_n_nums_helper(nums_copy, 0, len(nums_copy)-1)
    return nums_copy




def _segregate_p_n_nums_helper(nums:list, start:int, end:int):
    """
    Helper function to segregate positive and negative numbers in an array.

    This function uses a divide-and-conquer approach to segregate positive
    and negative numbers. The array is divided into subarrays recursively,
    segregated individually, and then combined back. This function
    is intended for internal use only and should not be called directly.

    Args:
        nums (list): The list of integers to be segregated.
        start (int): The starting index of the current segment of the list.
        end (int): The ending index of the current segment of the list.

    Returns:
        None
    """
    if start >= end:
        debug_print(f"Base case reached: start={start}, end={end}")
        return

    mid = (start + end) // 2
    debug_print(f"Dividing range [{start}:{end}] at mid={mid}")
    debug_print(f"  Left subarray: {nums[start:mid+1]} (indices {start} to {mid})")
    debug_print(f"  Right subarray: {nums[mid+1:end+1]} (indices {mid+1} to {end})")

    debug_print(f"Processing left half [{start}:{mid}]")
    _segregate_p_n_nums_helper(nums, start, mid)

    debug_print(f"Processing right half [{mid+1}:{end}]")
    _segregate_p_n_nums_helper(nums, mid + 1, end)

    debug_print(f"Merging subarrays [{start}:{mid}] and [{mid+1}:{end}]")
    _segregate(nums, start, mid, end)



def _segregate(nums, start, mid, end):
    """
    Processes the given range of the array by merging and segregating negative and positive integers
    from two subarrays within the range, ensuring that negative integers appear first in the merged
    result. The process involves comparing, ordering, and maintaining the intermediate and final state
    of the array during the segregation.

    Args:
        nums (List[int]): The input list of integers to be segregated and merged.
        start (int): The starting index of the range to be processed.
        mid (int): The midpoint index dividing the range into two subarrays.
        end (int): The ending index of the range to be processed.

    Returns:
        None
    """
    l_arr = nums[start:mid+1]
    r_arr = nums[mid+1:end+1]
    debug_print(f"  Left array: {l_arr}")
    debug_print(f"  Right array: {r_arr}")

    l, r, k = 0, 0, start
    step = 1

    while l < len(l_arr) and r < len(r_arr):
        debug_print(f"  Step {step}: Comparing l_arr[{l}]={l_arr[l]} with r_arr[{r}]={r_arr[r]}")

        if l_arr[l] > 0 >= r_arr[r]:
            debug_print(f"    {l_arr[l]} is positive and {r_arr[r]} is negative -> Place negative first")
            nums[k] = r_arr[r]
            debug_print(f"    nums[{k}] = {r_arr[r]}")
            r += 1
            k += 1
        else:
            debug_print(f"    Keeping current order -> Place {l_arr[l]}")
            nums[k] = l_arr[l]
            debug_print(f"    nums[{k}] = {l_arr[l]}")
            l += 1
            k += 1

        debug_print(f"    Current array state: {nums}")
        step += 1

    while l < len(l_arr):
        debug_print(f"  Step {step}: Copying remaining left element: {l_arr[l]}")
        nums[k] = l_arr[l]
        debug_print(f"    nums[{k}] = {l_arr[l]}")
        debug_print(f"    Current array state: {nums}")
        l += 1
        k += 1
        step += 1

    while r < len(r_arr):
        debug_print(f"  Step {step}: Copying remaining right element: {r_arr[r]}")
        nums[k] = r_arr[r]
        debug_print(f"    nums[{k}] = {r_arr[r]}")
        debug_print(f"    Current array state: {nums}")
        r += 1
        k += 1
        step += 1

    debug_print(f"  Merge complete for range [{start}:{end}]: {nums[start:end+1]}")
    debug_print("-" * 30)


