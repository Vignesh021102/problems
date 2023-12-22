class Solution:
  def __init__(self) -> None:
    self.diff1 = 0
    self.diff2 = 0
    
  def calculateDiff(self,a,b,c):
    self.diff1 = b - a - 1 
    self.diff2 = c - b - 1

  def min(self,a,b,c):
    self.calculateDiff(a,b,c)
    if self.diff1<0 or self.diff2<0:
      return 0

    if self.diff1 > self.diff2:
      if self.diff2 > 1:
        return 1 + self.min(b,b+1,c)
      else:
        return 1
    elif self.diff2 >= self.diff1 and self.diff1 != 0:
      if self.diff1 > 1:
        return 1 + self.min(a,a+1,b)
      else:
        return 1
    elif self.diff1 == 0 and self.diff2 != 0:
      return 1
    return 0
  
  def max(self,a,b,c):
    self.calculateDiff(a,b,c)
    return self.diff1 + self.diff2   

  def main(self,a,b,c):
    a,b,c = sorted([a,b,c])
    return [self.min(a,b,c),self.max(a,b,c)]
  
  #movement
  def __init__(self) -> None:
    self.result = [0,0]
  def recursive(self,a,b,c):
    self.diff1 = b - a - 1 
    self.diff2 = c - b - 1 
    print(a,b,c,self.diff1,self.diff2)
    if self.diff1<0 or self.diff2<0:
      return

    if self.diff1 > self.diff2:
      if self.diff2 > 1:
        self.result[0] += 1
        self.recursive(b+((c-b)//2),b,c)
      else:
        self.result[0] += 1
        return
    elif self.diff2 >= self.diff1 and self.diff1 != 0:
      if self.diff1 > 1:
        self.result[0] += 1
        self.recursive(a,b,a+((b-a)//2))
      else:
        self.result[0] += 1
        return
    elif self.diff1 == 0 and self.diff2 != 0:
      self.result[0] += 1
      return  
  def recursive2(self,a,b,c):
    self.diff1 = b - a - 1 
    self.diff2 = c - b - 1 
    print(a,b,c,self.diff1,self.diff2)
    if self.diff1<0 or self.diff2<0:
      return
    if self.diff1 < self.diff2:
      self.result[1] += 1
      if self.diff2 > 1:
        self.recursive2(b,b+((c-b)//2),c)
      else:
        return
    elif self.diff2 >= self.diff1 and self.diff1 != 0:
      self.result[1] += 1
      if self.diff1 > 1:
        self.recursive2(a,a+((b-a)//2),b)
      else:
        return     
  def main(self,a,b,c):
    a,b,c = sorted([a,b,c])
    self.recursive(a,b,c)
    print("high")
    self.recursive2(a,b,c)
    return self.result