from src.sorting.insertion_sort import insertion_sort



def test_insertion_sort():
    nums = [3, 2, 1, 5, 4]
    assert insertion_sort(nums) == [1, 2, 3, 4, 5]

    nums = [1, 2, 3, 4, 5]
    assert insertion_sort(nums) == [1, 2, 3, 4, 5]

    nums = [5, 4, 3, 2, 1]
    assert insertion_sort(nums) == [1, 2, 3, 4, 5]

    nums = []
    assert insertion_sort(nums) == []

    nums = [42]
    assert insertion_sort(nums) == [42]

    nums = [3, -1, 0, 2, -2, 1]
    assert insertion_sort(nums) == [-2, -1, 0, 1, 2, 3]
