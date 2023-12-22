import pytest
from home import Solution 

@pytest.fixture
def solution():
  return Solution()

def assert_unorderedList(list1, list2):
  assert list1 == list2


# Test cases
def test_case_1(solution):
  expected = [1,2] 
  assert_unorderedList(solution.main(1,5,2), expected)

def test_case_2(solution):
  expected = [0,0] 
  assert_unorderedList(solution.main(4,3,2), expected)

def test_case_3(solution):
  expected = [1,2] 
  assert_unorderedList(solution.main(3,5,1), expected)

def test_case_4(solution):
  expected = [2,4] 
  assert_unorderedList(solution.main(7,4,1), expected)

def test_case_4(solution):
  expected = [2,6] 
  assert_unorderedList(solution.main(1,9,5), expected)

def test_case_5(solution):
  expected = [2,22] 
  assert_unorderedList(solution.main(21,27,3), expected)