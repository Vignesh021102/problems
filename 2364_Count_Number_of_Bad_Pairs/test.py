import pytest
from main import Solution

def test_case1():
  solution = Solution()
  result = solution.main([4,1,3,3])
  assert result == 5

def test_case2():
  solution = Solution()

  result = solution.main([1,2,3,4,5])
  assert result == 0