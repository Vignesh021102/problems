import pytest
from main import Solution 

@pytest.fixture
def solution():
  return Solution()

def assert_unorderedList(list1, list2):
  print(list1,list2)
  assert list1 == list2


# Test cases
def test_case_1(solution):
  expected = True
  assert_unorderedList(solution.main([1,2,10,5,7]), expected)

def test_case_2(solution):
  expected = False
  assert_unorderedList(solution.main([2,3,1,2]), expected)

def test_case_3(solution):
  expected = False
  assert_unorderedList(solution.main([1,1,1]), expected)

def test_case_4(solution):
  expected = True
  assert_unorderedList(solution.main([1,1]), expected)
  
def test_case_5(solution):
  expected = True
  assert_unorderedList(solution.main([105,924,32,968]), expected)

def test_case_6(solution):
  expected = False
  assert_unorderedList(solution.main([2,3,4,5,1,5]), expected)

def test_case_7(solution):
  expected = True
  assert_unorderedList(solution.main([10,1,10]), expected)  