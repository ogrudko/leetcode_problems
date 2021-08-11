import pytest
from easy.pascal_triangle import Solution

cases = [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),  # happy path
    (0, []),     # zero-case
    (1, [[1]])    # one-case
]

@pytest.mark.parametrize('num_rows, result', cases)
def test_pascal_triangle(num_rows, result):
    solution = Solution()
    assert solution.generate(num_rows) == result