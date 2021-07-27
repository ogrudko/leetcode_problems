import pytest
from easy.implement_index import Solution

def test_one_needle_one_char():
    solution = Solution()
    assert solution.strStr("hello world", "w") == 6