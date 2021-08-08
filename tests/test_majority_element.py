from typing import List
import pytest
from easy.majority_element import Solution

cases = [
    ([1, 2, 2, 2, 2, 2, 2, 2, 1, 1], 2),    # happy path
    ([], 0),    # empty list
    ([1], 1),    # only one element
    ([1, 1], 1), # all elements are the same
    ([1, 2], 0), # no major element
    ([1, 1, 1, 2, 2, 3, 3], 0),   # prevailing element but not major
    ([1, 1, 1, 2, 2, 2, 3, 3, 3], 0),   # no major or even prevailing element
    (['non', 'digits'], 0)  # non-digits
]

@pytest.mark.parametrize('nums, result', cases)
def test_majority_element(nums, result):
    solution = Solution()
    assert solution.majority_element(nums) == result