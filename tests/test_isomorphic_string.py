import pytest
from easy.isomorphic_string import Solution

cases = [
    ('egg', 'add', True),
    ('foo', 'bar', False),
    ('paper', 'title', True),
    ('badc', 'baba', False)
]

@pytest.mark.parametrize('s, t, result', cases)
def test_isomorphic_string(s: str, t: str, result: bool):
    solution = Solution()
    assert solution.is_isomorphic(s, t) == result