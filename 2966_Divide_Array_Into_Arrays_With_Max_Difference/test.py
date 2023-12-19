
import pytest
from hash import Solution


def test_case_1():

  solution = Solution()
  result = solution.divideArray([1,3,4,8,7,9,3,5,1],3) 

  assert result == [[1,1,3],[3,4,5],[7,8,9]]
def test_case_2():

  solution = Solution()
  result = solution.divideArray([1,3,3,2,7,3],3) 

  assert result == []
