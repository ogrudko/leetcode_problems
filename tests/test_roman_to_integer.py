import pytest
from easy.roman_to_integer import Solution

cases = [
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('C', 100),
    ('D', 500),
    ('M', 1000),
    ('L', 50),
    ('A', 0),
    ('IV', 4),
    ('VI', 6),
    ('IIII', 4),
    ('MCMXCIV', 1994),
    ('MCMXCVIII', 1998),
    ('MCMXCVOI', 0),
    ('MCMXCVII1', 0)
]

@pytest.mark.parametrize('roman, result', cases)
def test_roman_to_int(roman, result):
    solution = Solution()
    assert solution.roman_to_int(roman) == result