import pytest
from easy.search_insert_position import Solution

cases = [
    ([1,3,5,6], 5, 2), # inserting in the middle of array (values exists in array)
    ([1,3,5,6], 2, 1),  # inserting in the middle of array )value is not in the array)
    ([1,3,5,6], 7, 4),  # inserting at the end of the array
    ([1,3,5,6], 0, 0),  # inserting at the beginning of the array
    ([1], 0, 0),    # array has only one item
    ([], 4, 0), # array is empty
    ([2,7,8,9,10], 'a', -1) #inserting non-integer
]

@pytest.mark.parametrize('nums, target, result', cases)
def test_search_insert_position(nums, target, result):
    solution = Solution()
    assert solution.search_insert(nums, target) == result