import pytest
from easy.column_number import Solution

cases = [
    ('A', 1),
    ('Z', 26),
    ('AA', 27),
    ('ZY', 701),
    ('FXSHRXW', 2147483647),
    (15, -1),
    (['A'], -1),
    ({'A': 1}, -1),
    ('1', -1),
    ('*', -1),
    ('AB*', -1)
]

@pytest.mark.parametrize('column_title, output', cases)
def test_title_to_number(column_title: str, output: int):
    solution = Solution()
    assert solution.title_to_number(column_title) == output