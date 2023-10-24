#problem Statement:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# def twoSum(num,target):
#   for i in  range(len(nums)-1):
#     temp = target - nums[i]
#     for j in range(i+1,len(nums)):
#         if nums[j] == temp:
#             return [i,j]
def wordBreak( s: str, wordDict: list[str]) -> bool:
  dp = [True] + [False] * (len(s))
  for i in range(len(s)):
      for j in range(i, len(s)):
        if s[i:j+1] in wordDict:
          dp[j+1] = dp[i] or dp[j+1]
        print(i,j,s[i:j+1],dp[i],dp[j+1],"dp ==",dp)
  print(dp[-1])
  return dp[-1]

wordBreak("catsandog",["cats","dog","sand","and","cat"])