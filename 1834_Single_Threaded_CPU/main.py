from heap import MinHeap

class Solution:
  def main(self,tasks:list[list[int]]) -> list[int]:
    tasks = [x+[i] for i,x in enumerate(tasks)]
    tasks.sort(key=lambda x:x[0])
    nTasks = len(tasks)
    print(tasks)
    heap = MinHeap()
    result = []
    time = tasks[0][0]
    maxTime = tasks[0][0]
    index = 0
    temp = None
    while  time <= maxTime:
      print( )

      while index < nTasks:
        if tasks[index][0] == time:
          print(tasks[index],index)
          heap.addNode(tasks[index][0],tasks[index][1],tasks[index][2])
          index+=1
        else:
          break
      print(time == maxTime,time,maxTime)
      if time == maxTime:
        temp = heap.removeNode()
        if not temp : 
          time+=1
          continue
        maxTime = time + temp['duration']
        result.append(temp['index'])
        print(time,maxTime,temp)

      if index < nTasks:
        time += 1
      else:
        time = maxTime
    return result