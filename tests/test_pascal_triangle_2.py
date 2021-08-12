import pytest
from easy.pascal_triangle_2 import Solution

cases = [
    (3, [1,3,3,1]),
    (0, [1]),
    (1, [1,1])
]

@pytest.mark.parametrize('row_index, result', cases)
def test_get_row(row_index, result):
    solution = Solution()
    assert solution.get_row(row_index) == result