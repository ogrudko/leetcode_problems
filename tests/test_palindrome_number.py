import pytest
from easy.palindrome_number import Solution


cases = [
    (0, True), # zero as an edge case
    (5, True), # 1-digit as an adge case
    (14, False), # even-digit false case
    (33, True), # even-digit True case
    (131, True),    # odd-digit True case
    (245, False),    # odd-digit False case
    ('222', False),  # non-integer case
    (True, False),   #boolean edge case
    (-1221, False)  # negative number, but almost a palindrome
]

@pytest.mark.parametrize('x, result', cases)
def test_palindrome_number(x, result):
    solution = Solution()
    assert solution.is_palindrome(x) == result