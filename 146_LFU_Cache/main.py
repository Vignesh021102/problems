#linked list approch

class Node:
  def __init__(self,key:int,value:int) -> None:
    self.value = value
    self.key = key
    self.next = None
    self.parent = None
    self.count = 1
  def __repr__(self) -> str:
    return f" << {self.parent.key if self.parent else None} <P- {self.key}={self.count}={self.value} -N>> {self.next}"


class LFUCache:
  def __init__(self,capacity) -> None:
    self.capacity = capacity
    self.size = 0
    self.head = None
    self.tail = None
    self.keyHash = {}
    self.countHash = {}
  def __insertBehind__(self,base:Node,temp:Node) -> None:
    if base.key == temp.key:
      return None
    
    if temp.next:
      temp.next.parent = temp.parent
    
    #next pointers
    base.next,temp.next = temp,base.next
    
    #parent pointers
    temp.parent = base

  def __increaseCounter__(self,temp:Node)->None:
    #scenarios:
    #temp is a self.head
    #temp is at self.tail
    #temp is at head of counter Hash
    #temp is in middle of a linked list

    #merge scenarios:
    #node at counter+1 is present 
    #node at counter+1 not found 

    if temp.key == self.head.key:
      temp.count += 1
      self.countHash[temp.count] = temp
      self.countHash[temp.count-1] = temp.next
      return None
    try:
      target = self.countHash[self.countHash[temp.count].parent.count]
    except:
      target = self.head

    if temp.key == self.countHash[temp.count].key:
      self.countHash[temp.count] = temp.next
    

    self.__moveTailForward__(temp)
    self.__insertBefore__(target,temp)
    self.countHash[temp.count+1] = temp
    temp.count+=1
    return None
    
  def __moveTailForward__(self,temp) -> None:
    if self.tail.parent == None:
      return None
    
    if self.tail:
      if temp.key == self.tail.key:
        #move up
        #cutting ties
        # if self.tail.next:
        #   self.tail.next.parent = None
        self.tail = self.tail.parent    
        
        self.tail.next = None
    return None
  
  def __insertBefore__(self,base:Node,temp:Node)->None:
    temp.next = base
    temp.parent = base.parent
    if base.parent:
      if base.parent.key != temp.key:
        base.parent.next = temp
    
    base.parent = temp
    #setting the count 

    if self.head.key == base.key:
      self.head = temp

    return None

  def put(self,key:int,value:int) -> None:
    #adding 
    if self.size >= self.capacity:
      #moving tail up (removing last node)
      del self.keyHash[self.tail.key]
      self.__moveTailForward__(self.tail)
      self.size -= 1


    if not self.head:
      self.head = Node(key = key,value= value)
      self.tail = self.head

      self.size += 1
      #hash
      self.keyHash[key] = self.head
      self.countHash[1] = self.head

      return None
    
    if key in self.keyHash:
      #updating the key if it exist

      self.keyHash[key].value = value
      self.__increaseCounter__(self.keyHash[key])
      # self.__searchUpdate(key=key,value = value)
      return None
    
    #first time this key appears
    temp = Node(key = key,value= value)

    if 1 in self.countHash:
      self.__insertBefore__(self.countHash[1],temp)
      self.countHash[1] = temp
    else:
      self.__insertBehind__(self.tail,temp)

    self.keyHash[key] = temp
    self.size += 1
    
    
    return None

  def get(self,key:int) -> int:
    if self.head == None:
      return -1
    
    if self.head.key == key:
      return self.head.value

    if key in self.keyHash:
      self.__increaseCounter__(self.keyHash[key])

      return self.keyHash[key].value
    
    return -1
