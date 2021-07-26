import pytest
from easy.longest_common_prefix import Solution


def test_common_prefix_all_str():
    solution = Solution()
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"

def test_no_common_prefix():
    solution = Solution()
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ""

def test_common_prefix_in_some_strings():
    solution = Solution()
    assert solution.longestCommonPrefix(["racecar","racer", "dog"]) == ""

def test_empty_list():
    solution = Solution()
    assert solution.longestCommonPrefix([]) == ""

def test_one_string():
    solution = Solution()
    assert solution.longestCommonPrefix(["word",]) == "word"

def test_common_but_not_prefix():
    solution = Solution()
    assert solution.longestCommonPrefix(["driver", "cabdriver"]) == ""