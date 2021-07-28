import pytest
from easy.add_binary import Solution

cases = [
    ("11", "11", "110"),    # case 1: binaries of the same length
    ("11", "1", "100"),     # case 2: first binary is longer
    ("1", "11", "100"),     # case 3: second binary is longer
    ("11100101010", "1001010101010", "1100111010100"),   # case 4: random binraies to trigger ifs
    ("1010", "", "1010")    # case 5: one of the binaries is empty string
]


@pytest.mark.parametrize('a, b, c', cases)
def test_add_binary(a, b, c):
    solution = Solution()
    assert solution.add_binary(a, b) == c

def test_int_type_error_exception():  # case 6: one of the binaries is an integer (non-iterable type)
    solution = Solution()
    with pytest.raises(TypeError):
        solution.add_binary("100", 100, "100")

def test_list_type_error_exception():  # case 7: one of the binaries is not a list (iterable type)
    solution = Solution()
    with pytest.raises(TypeError):
        solution.add_binary("100", ["10", "1", "11"], "100")

