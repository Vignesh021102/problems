class Solution:
  def main(self,nums)->bool:
    isDent = False
    for i in range(len(nums)-1):
     if nums[i] >= nums[i+1]:
      #dent found 
      if isDent:
        return False
      else:
        isDent = True


      if i+2 < len(nums):
        if nums[i] > nums[i+2]:
          #remove i; it's the bump
          if i-1 >= 0:
            if not nums[i-1] < nums[i+1]:
              return False
          else:
            continue
        elif nums[i] == nums[i+2]:
          if i == 0 or i+2 == len(nums):
            continue
          return False
        else:
          #remove i+1; it's the dip
          if nums[i+1]<nums[i+2]:
            i+=1
            continue
            # if i-1 >= 0:
            #   if not nums[i-1] < nums[i+1]:
            #     return False
            # else:
            #   continue
          else:
            return False
    return True

#online: not mine ;)
# class Solution:
#     def main(self, nums: list[int]) -> bool:
#         needToBeRemoved = 0
#         for i in range(1, len(nums)):
#             if nums[i] <= nums[i - 1]:
#                 needToBeRemoved += 1
#                 if i > 1 and nums[i] <= nums[i - 2]:
#                     nums[i] = nums[i - 1]
            
        
#         return needToBeRemoved < 2