'''
set of parametrized test cases to verify functional correctnes of missing_number.py solution
'''
import pytest
from easy.missing_number import Solution

cases = [
    ([3,0,1], 2),
    ([0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
    ([0], 1),
    ([1], 0),
    ([1, 2], 0)
]

@pytest.mark.parametrize('nums, result', cases)
def test_missing_number(nums, result):
    '''
    test designed to verify functional correctness of missing_number.py solution
    '''
    solution = Solution()
    assert solution.missing_number(nums) == result
