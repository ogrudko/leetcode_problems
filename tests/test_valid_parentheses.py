import pytest
from easy.valid_parentheses import Solution

cases = [
    ('', True),
    (' ', True),
    ('(', False),
    ('}', False),
    ('[]', True),
    ('{ ', False),
    ['{]', False],
    ('}{,', False),
    ('[]{}()', True),
    ('[{()}]', True),
    ('[()([]){[()([()])]}]', True),
    ('{}{', False),
    ('[]]]', False)
]

@pytest.mark.parametrize('user_string, result', cases)
def test_valid_parentheses(user_string, result):
    solution = Solution()
    assert solution.is_valid_parentheses(user_string) == result