class Node:
  def __init__(self,time = 1,duration = 1,index = None):
    self.left = None
    self.right = None
    self.time = time
    self.duration = duration
    self.index = index
  def __str__(self) -> str:
    if self.left == None and self.right == None:
      return f" {self.time}-{self.index}-{self.duration} "
    
    return f"{self.time},{self.duration} =L>{self.left} =R>{self.right}"
# RecursionError: maximum recursion depth exceeded
class MinHeap:
  def __init__(self):
    self.root = None
  def addNode(self,time,duration,index):
    temp = Node(time = time,duration = duration,index = index)
    # print(temp)
    if self.root == None:
      self.root = temp
    else:
      self.__insertNode(self.root,temp)
    
    # print("ROOT",self.root)
  def removeNode(self):
    if not self.root:
      return None 
    time = self.root.time
    duration = self.root.duration
    index = self.root.index
    self.root = self.__deleteNode(self.root)
    # print("ROOT",self.root)
    return {"time":time,"duration":duration,"index":index}
  def __swapNode(self,node1,node2):
    node1.time,node2.time = node2.time,node1.time
    node1.duration,node2.duration = node2.duration,node1.duration
    node1.index,node2.index = node2.index,node1.index
  def __copy(self,baseNode, copyNode):
    baseNode.time = copyNode.time
    baseNode.duration = copyNode.duration
    baseNode.index = copyNode.index
  def __insertNode(self,head,temp):
    #insertion and swapping
    if temp.duration > head.duration:
      #right
      if head.right == None:
        head.right = temp
      else:
        self.__insertNode(head.right,temp)

      if head.duration > head.right.duration:
        self.__swapNode(head,head.right)
    elif temp.duration < head.duration:
      #left
      if head.left == None:
        head.left = temp
      else:
        self.__insertNode(head.left,temp)
      
      if head.duration >= head.left.duration:
        self.__swapNode(head,head.left)
    elif temp.index < head.index:
      if head.left == None:
        head.left = temp
      else:
        self.__insertNode(head.left,temp)
      
      if head.duration >= head.left.duration:
        self.__swapNode(head,head.left)
    else:
      #right
      if head.right == None:
        head.right = temp
      else:
        self.__insertNode(head.right,temp)

      if head.duration > head.right.duration:
        self.__swapNode(head,head.right)
    return
  def __leftMost(self,head,temp):
    if head.left == None:
      return head
    if head.left.left == None:
      temp = head.left
      head.left = None
      return temp
    else:
      return self.__leftMost(head.left)
  def __deleteNode(self,head):
    if head.left and head.right:
      if head.left.duration < head.right.duration:
        self.__copyDelLeft(head)
      elif head.left.duration == head.right.duration:
        if head.left.index < head.right.index:
          self.__copyDelLeft(head)
        else:
          self.__copyDelRight(head)
      else:
        self.__copyDelRight(head)
    elif (not head.left) and (not head.right):
      return None
    elif not head.left:
      self.__copyDelRight(head)
    elif not head.right:
      self.__copyDelLeft(head)
    return head
  def __copyDelLeft(self,head):
    self.__copy(head,head.left)
    head.left = self.__deleteNode(head.left)
  def __copyDelRight(self,head):
    self.__copy(head,head.right)
    head.right = self.__deleteNode(head.right)