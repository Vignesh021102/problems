import pytest
from main import Solution 

@pytest.fixture
def solution():
  return Solution()

def assert_unorderedList(result, expected):
  assert result == expected


# Test cases
def test_case_1(solution):
  expected = 3
  assert_unorderedList(solution.main(nums=[3,2,5,4],threshold=5), expected)

def test_case_2(solution):
  expected = 1
  assert_unorderedList(solution.main(nums=[1,2],threshold = 2), expected)

def test_case_3(solution):
  expected = 3
  assert_unorderedList(solution.main(nums=[2,3,4,5],threshold = 4), expected)

def test_case_4(solution):
  expected = 1
  assert_unorderedList(solution.main(nums=[2,2,2,2],threshold = 4), expected)
  
def test_case_5(solution):
  expected = 0
  assert_unorderedList(solution.main(nums=[1,1,1,1],threshold = 2), expected)

def test_case_6(solution):
  expected = 2
  assert_unorderedList(solution.main(nums=[4,10,3],threshold = 10), expected)

