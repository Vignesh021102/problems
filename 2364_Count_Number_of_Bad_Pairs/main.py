class Solution:
  # countBadPairs
  def brute_force(self, nums: list[int]) -> int:
    result = 0
    for i in range(0,len(nums)):
      for j in range(i,len(nums)):
        if i < j and j-i != nums[j] - nums[i]:
          result += 1
    return result