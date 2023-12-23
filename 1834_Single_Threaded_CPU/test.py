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
  expected = [0,2,3,1]
  assert_unorderedList(solution.main([[1,2],[2,4],[3,2],[4,1]]), expected)

def test_case_2(solution):
  expected = [4,3,2,0,1]
  assert_unorderedList(solution.main([[7,10],[7,12],[7,5],[7,4],[7,2]]), expected)

def test_case_3(solution):
  expected = [6,1,2,9,4,10,0,11,5,13,3,8,12,7]
  assert_unorderedList(solution.main([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]), expected)



# from heap import MinHeap

# class Solution:
#   def main(self,tasks:list[list[int]]) -> list[int]:
#     tasks.sort(key=lambda x:x[0])
#     nTasks = len(tasks)
#     print(tasks)
#     heap = MinHeap()
#     result = []
#     time = 1
#     maxTime = 1
#     index = 0
#     temp = None
#     count = 0
#     while  count < nTasks:
#       print(time)
#       index = 0
#       while index < nTasks:
#         if tasks[index][0] == time:
#           print(tasks[index],index)
#           heap.addNode(tasks[index][0],tasks[index][1],index)
#           index+=1
#           count+=1
#         else:
#           break
#       print(time == maxTime,time,maxTime)
#       if time == maxTime:
#         temp = heap.removeNode()
#         if not temp : 
#           time+=1
#           continue
#         maxTime = time + temp['duration']
#         result.append(temp['index'])
#         print(time,maxTime,temp)

#       time += 1
#       count+=1
#       print(time,maxTime,"NOW")
#     return result