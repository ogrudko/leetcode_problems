import pytest
from easy.last_word_length import Solution

cases = [
    ('hello world', 5),  # case 1: last word, ordinary number
    ('hello V', 1),  # case 2: last word, one char
    ('hello world ', 5), # case 3: extra space at the end of the string
    ('', 0), # case 4: empty string
    ('    ', 0) # case 5: string consists only of spaces
]


@pytest.mark.parametrize('string, result', cases)
def test_length_of_last_word(string, result):
    solution = Solution()
    assert solution.length_of_last_word(string) == result




