import pytest
from easy.best_time_for_profit import Solution

cases = [
    ([7,1,5,3,6,4], 5),     # happy path
    ([7,6,4,3,1], 0),       # prices go only worse
    ([], 0),     # no trading yet
    ([1], 0),    # first day of trading
    ([2,4,1], 2)   # max profit from the day one, but min price drops the other day
]

@pytest.mark.parametrize('prices, max_profit', cases)
def test_best_time_for_profit(prices, max_profit):
    solution = Solution()
    assert solution.max_profit(prices) == max_profit