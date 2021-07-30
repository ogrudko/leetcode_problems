import pytest
from easy.merge_sorted_lists import Solution

cases = [
    ([1, 2, 3], [0, 2, 4], [0, 1, 2, 2, 3, 4]), # happy path
    ([1, 2, 3], [], [1, 2, 3]),  # one list is empty
    ([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]),  # two identical lists
    ([1, 2, 3], [1, 1, 1], [1, 1, 1, 2, 1, 3])  # resulting array is not sorted
]

@pytest.mark.parametrize('first_list, second_list, result', cases)
def test_merge_sorted_lists(first_list, second_list, result):
    solution = Solution()
    assert solution.merge_sorted_lists(first_list, second_list) == result