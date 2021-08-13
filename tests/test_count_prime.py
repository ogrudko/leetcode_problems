import pytest
from easy.count_prime import Solution

cases = [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 2),
    (5, 3),
    (6, 3),
    (7, 4),
    (8, 4),
    (10, 4),
    (11, 5),
    (20, 8)
]

@pytest.mark.parametrize('count_primes, result', cases)
def test_count_primes(count_primes, result):
    solution = Solution()
    assert solution.count_primes(count_primes) == result