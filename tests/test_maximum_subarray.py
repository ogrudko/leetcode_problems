import pytest
from easy.maximum_subarray import Solution

cases = [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),    # positive and negative numbers
    ([1], 1),   # one number
    ([5,4,-1,7,8], 23),    #all numbers are in subarray
    ([-2,-1,-3,-4,-1,-2,-1,-5,-4], -1),  # all negatives
    ([-1, -2, -3, -4, -5], -1)  # the sum always decreases
]

@pytest.mark.parametrize('nums, result', cases)
def test_max_sub_array(nums, result):
    solution = Solution()
    assert solution.max_sub_array(nums) == result

