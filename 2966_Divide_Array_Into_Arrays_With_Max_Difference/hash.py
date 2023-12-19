class Solution:
  def removeElement(self,arr,index):
    return arr[:index]+arr[index+1:]
  def check(self,temp,num,k):
    for i in temp:
      if not (num-i >= -2 and num-i <= 2):
        return False
    return True
  def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
    nums.sort()
    index = 0
    result = []
    temp = []
    while index < len(nums):
      
      if len(temp) == 0:
        temp.append(nums[index])
        nums = self.removeElement(nums,index)
        index -= 1
      elif  self.check(temp,nums[index],k):
        temp.append(nums[index])
        nums = self.removeElement(nums,index)
        index -= 1
      if len(temp) == 3:
        result.append(temp)
        temp = []
        index = -1
      index+= 1
      
    if len(nums) > 0 or len(temp) > 0:
      return []
    else:
      return result