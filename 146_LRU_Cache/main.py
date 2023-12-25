#linked list approch

class Node:
  def __init__(self,key:int,value:int) -> None:
    self.value = value
    self.key = key
    self.next = None
    self.parent = None
  def __repr__(self) -> str:
    return f" << {self.parent.key if self.parent else None} <P- {self.key}={self.value} -N>> {self.next}"


class Solution:
  def __init__(self,capacity) -> None:
    self.capacity = capacity
    self.size = 0
    self.head = None
    self.tail = None
    self.hash = {}
  def __moveTohead(self,temp:Node) -> None:
    #moving tail to parent if it's in temp
        if self.tail:
          if self.tail.key == temp.key:
            self.tail = self.tail.parent

          #cutting ties
          if self.tail.next:
            self.tail.next.parent = None
            self.tail.next = None
          
        #moving to top
        if temp.parent:
          temp.parent.next = temp.next
        if temp.next:
          temp.next.parent = temp.parent
  
        temp.next = self.head
        self.head.parent = temp
        self.head = temp
        
        temp.parent = None
  
  def __searchUpdate(self,key:int,value:int) -> bool:
    if self.head.key == key:
      self.head.value = value
      return True
    temp = self.head.next

    while temp != None:
      if temp.key == key:
        temp.value = value
        self.__moveTohead(temp)
        return True
      temp = temp.next
    return False
  
  def put(self,key:int,value:int) -> None:
    print("daw")
    
    #adding 
    if not self.head:
      self.head = Node(key = key,value= value)
      self.tail = self.head
      self.size += 1
      self.hash[key] = True
      return None
    
    if key in self.hash:
      self.__searchUpdate(key=key,value = value)
      return None
    

    temp = Node(key = key,value= value)
    temp.next = self.head
    self.head.parent = temp
    self.head = temp 
    
    self.hash[key] = True
    self.size += 1
    
    if self.size > self.capacity:
      #moving tail up (removing last node)
      del self.hash[self.tail.key]
      self.tail = self.tail.parent
      self.tail.next.parent = None
      self.tail.next = None
      self.size -= 1
    
    return None

  def get(self,key:int) -> int:
    if self.head == None:
      return -1
    
    if self.head.key == key:
      return self.head.value

    if key in self.hash:
      temp = self.head.next
      while temp != None:
        if temp.key == key:

          self.__moveTohead(temp)
          
          return temp.value
        temp = temp.next
    
    return -1
  
    