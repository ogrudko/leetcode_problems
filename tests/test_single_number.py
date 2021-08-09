import pytest
from easy.single_number import Solution


cases = [
    ([2,2,1], 1),   # happy path
    ([4,1,2,1,2], 4),   # happy path 2
    ([4, 4, 1, 2, 2], 1),    #happy path 3
    ([1], 1),    # one element
    ([], 0),     # empty input
    ({1, 2, 3}, 0),   # invalid object type
    (['1', '2', '3'], -1),   # invalid iterable elements type
    ([1, 2, 3], -2),     # multiple single elements
    ([1, 1, 2, 2], 0)  # no single element

]

@pytest.mark.parametrize('nums, result', cases)
def test_single_number(nums, result):
    solution = Solution()
    assert solution.single_number(nums) == result