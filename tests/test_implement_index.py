import pytest
from easy.implement_index import Solution

cases = [
    ('hello world', 'w', 6),    # case 1: needle in the haystack, one char
    ('hello world', 'wo', 6),   # case 2: needle in the haystack, two chars
    ('hello world', 'hello world', 0),  # case 3: needle equals haystack
    ('hello world', '', 0), # case 4: no needle at all
    ('', 'world', 0),   # case 5: empty haystack
    ('hello world', 'o', 4),    # case 6: multiple needles in the haystack
    ('hello world', 'car', -1),  # case 7: needle is not in the haystack
    ('hello world', 'hello world!', -1) #needle is bigger than the haystack
]


@pytest.mark.parametrize('haystack, needle, result', cases)
def test_one_needle_one_char(haystack, needle, result):
    solution = Solution()
    assert solution.str_str(haystack, needle) == result