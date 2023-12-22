import pytest
from Sum import Solution  # Replace 'solution_file' with the correct module name
from collections import Counter

# Creating an instance of the Solution class
@pytest.fixture
def solution():
    return Solution()

# Function to assert unordered list equality
def assert_unorderedList(list1, list2):
    assert list1 == list2

    # print(list1,list2)
    # counter1 = Counter(list1)
    # counter2 = Counter(list2)
    # assert counter1 == counter2, "Lists are not equal"

# Test cases
def test_case_1(solution):
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]  # Expected list of unordered inner lists
    assert_unorderedList(solution.main(nums), expected)

def test_case_2(solution):
    nums = [0, 1, 1]
    expected = []  # Expected empty list
    assert_unorderedList(solution.main(nums), expected)

def test_case_3(solution):
    nums = [0, 0, 0]
    expected = [[0, 0, 0]]  # Expected list with a single unordered inner list
    assert_unorderedList(solution.main(nums), expected)

def test_case_4(solution):
    nums = [1, 2, -2, -1]
    expected = []  # Expected empty list
    assert_unorderedList(solution.main(nums), expected)