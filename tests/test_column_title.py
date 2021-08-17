import pytest
from easy.column_title import Solution

cases = [
    (1, 'A'),
    (15, 'O'),
    (26, 'Z'),
    (28, 'AB'),
    (701, 'ZY'),
    (2147483647, 'FXSHRXW')
]

@pytest.mark.parametrize('column_number, output', cases)
def test_column_title(column_number: int, output: str):
    solution = Solution()
    assert solution.convert_to_title(column_number) == output