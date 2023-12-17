# https://leetcode.com/problems/check-if-the-number-is-fascinating/

# You are given an integer n that consists of exactly 3 digits.

# We call the number n fascinating if, after the following modification, the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:

# Concatenate n with the numbers 2 * n and 3 * n.
# Return true if n is fascinating, or false otherwise.

# Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

class Solution:
    def __init__(self) -> None:
      self.hash = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    def addToHash(self,n):
      for i in str(n):
        if i == '0' or self.hash[i] > 0:
          return False
        else:
          self.hash[i] += 1
      return True
    def isFascinating(self, n: int) -> bool:
      if n <= 100 or n >= 999:
        return False
      # by default the input is 100 < n < 999  
      if n%10 == 0:
        return False
      return self.addToHash(n) & self.addToHash(n*2) & self.addToHash(n*3)
    
print(Solution().isFascinating(100))
print(Solution().isFascinating(192))
print(Solution().isFascinating(984))