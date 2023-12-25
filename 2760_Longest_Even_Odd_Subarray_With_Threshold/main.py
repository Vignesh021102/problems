class Solution:
  def main(self,nums:list[int],threshold)->int:
    def isEven(n):
      return nums[n]%2 == 0 
    count = 0
    maxCount = 0
    isOnRecord = False
    l = 0
    r = -1
    for i in range(len(nums)):
      if isOnRecord:
        if (not (isEven(r) ^ isEven(r+1))) or nums[i]>threshold:
          count = (r - l) + 1 
          maxCount = count if maxCount < count else maxCount
          isOnRecord = False
        else:
          r+=1
      if not isOnRecord:
        if isEven(i) and nums[i] <= threshold:
          isOnRecord = True
          l = i
          r = i
    count = (r-l)+1
    return count if maxCount < count else maxCount