from heap import MinHeap

class Solution:
  def main(self,tasks:list[list[int]]) -> list[int]:
    # tasks = [x+[i] for i,x in enumerate(tasks)]
    # tasks.sort(key=lambda x:x[0])
    # nTasks = len(tasks)
    time = -1 
    for i in range(0,len(tasks)):
      if time > tasks[i][0] or time == -1:
        time = tasks[i][0]
      tasks[i] = tasks[i]+[i]

    print(tasks)
    heap = MinHeap()
    result = []
    maxTime = time
    index = 0
    temp = None
    lastTime = 0
    while  time <= maxTime:
      # print(time,maxTime,index,"index")
      index = 0
      while index < len(tasks):
        print(time,lastTime,tasks[index],tasks,tasks[index][0] <= time and tasks[index][0] > lastTime)
        if tasks[index][0] <= time and tasks[index][0] > lastTime:
          # print(tasks[index],index,"inserted")
          heap.addNode(tasks[index][0],tasks[index][1],tasks[index][2])
          tasks = tasks[:index]+tasks[index+1:]
          index -= 1  
        index+=1

      print(time == maxTime,time,maxTime)
      if time == maxTime:
        # print(heap.root)
        temp = heap.removeNode()
        if not temp : 
          time+=1
          continue
        maxTime = time + temp['duration']
        result.append(temp['index'])
        # print(time,maxTime,temp)
      # print(time,maxTime)
      lastTime = time
      time = maxTime
    return result
  
Solution().main([[1,3],[2,5],[3,1]])