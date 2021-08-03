import pytest
from easy.plus_one import Solution

cases = [
    ([1, 2, 3], [1, 2, 4]), # adding to any nnumber
    ([0], [1]), # adding to zero
    ([9], [1, 0]),  # adding over ten
    ([9, 9], [1, 0, 0]),    # adding over hundred
    ([9, 9, 9, 9, 9], [1, 0, 0, 0, 0, 0]),   # adding over hundred thousand
    ([3, 1, 9], [3, 2, 0])  #   adding over ten insinde the numebr
]

@pytest.mark.parametrize('digits, result', cases)
def test_plus_one(digits, result):
    solution = Solution()
    assert solution.plus_one(digits) == result
