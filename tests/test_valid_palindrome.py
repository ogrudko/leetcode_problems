import pytest
from easy.valid_palindrome import Solution

cases = [
    ('A man, a plan, a canal: Panama', True),
    ('raceacar', False),
    ('Aerate pet area.', True),
    ('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!', True),
    ('Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era.', True),
    ('As I pee, sir, I see Pisa!', True),
    (',.', True),
    ('0P', False)
]


@pytest.mark.parametrize('s, result', cases)
def test_valid_palindrome(s, result):
    solution = Solution()
    assert solution.is_palindrome(s) == result