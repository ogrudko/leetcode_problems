import pytest
from easy.remove_element import Solution

cases = [
    ([1, 2, 3, 4], 2, [1, 3, 4]), # one removeal
    ([3, 2, 2, 3], 2, [3, 3]),    # two removals
    ([1, 2, 3, 4], 5, [1, 2, 3, 4]),  # zero removals
    ([1, 1, 1, 1, 1], 1, []), # removing whole array
    ([1, 2, 3, 4], 1, [2, 3, 4]),  # removing 0-th element
    ([1, 2, 3, 4], 4, [1, 2, 3]),  # removing last element
    ([1, 2, 3, 2, 1], 1, [2, 3, 2])   #removing 0-th and last element
    ]



@pytest.mark.parametrize('nums, val, result', cases)
def test_remove_element(nums, val, result):
    solution = Solution()
    assert solution.remove_element(nums, val) == result