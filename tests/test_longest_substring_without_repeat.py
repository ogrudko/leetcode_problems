'''
set of parametrized test cases to verify functional correctnes of longest_substring_without_repeat.py solution
'''
import pytest
from easy.longest_substring_without_repeat import Solution

cases = [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('', 0),
    ('abcaqzwdb', 7),
    ('tmmzuxt', 5),
    ('ohvhjdml', 6)
]

@pytest.mark.parametrize('s, result', cases)
def test_length_of_longest_substring(s: str, result: int):
    solution = Solution()
    assert solution.length_of_longest_substring(s) == result