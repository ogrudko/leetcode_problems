import pytest
from easy.remove_duplicates_in_sorted_array import Solution

cases = [
    ([1, 2, 2, 3, 4], False),    # duplicate inside the array
    ([1, 1, 2, 3], False),  # duplicate at the beginning of array
    ([1, 2, 3, 4, 4], False),   # duplicate at the end of array
    ([1, 2, 3, 4], False),  # no duplicate
    ([1, 1, 2, 2, 3, 4], False) # two duplicates
]

@pytest.mark.parametrize('nums, result', cases)
def test_remove_duplicates_in_sorted_array(nums, result):
    solution = Solution()
    is_duplicate = False
    i, no_dupes_nums = solution.remove_duplicates(nums)
    for k in range(i - 1):
        if no_dupes_nums[k] == no_dupes_nums[k + 1]:
            is_duplicate = True
    assert is_duplicate == result
