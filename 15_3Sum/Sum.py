class Solution:
  def brute_force(self, nums: list[int]) -> list[list[int]]:
    result = []
    n = len(nums)
    temp = []
    for i in range(0,n-2):
      for j in range(i+1,n-1):
        for k in range(j+1,n):
          temp = [[nums[i],nums[j],nums[k]]]
          temp[0].sort()
          if nums[i]+nums[j]+nums[k] == 0:
            if temp[0] not in result:
              result = temp + result
    return result
  def seperateCount(self, nums: list[int]) -> list[list[int]]:
    P = []
    N = []
    Z = 0

    for i in nums:
      if i > 0:
        P.append(i)
      elif i < 0:
        N.append(i)
      else:
        Z += 1
    
  
    result = set()
    if Z >= 3:
      result.add(tuple([0,0,0]))
    
    print(P,N,Z)
    #for each zero
    for i in range(0,Z):
      for j in P:
        for k in N:
          if j == -1 * k:
            result.add(tuple(sorted([j,0,k])))
    target = 0

    print(result)
    for i in range(0,len(P)-1):
      for j in range(i+1,len(P)):
        target = -1*(P[i]+P[j])
        if target in N:
          print(P[i],P[j],target)
          result.add(tuple(sorted([P[i],P[j],target])))

    print(result)
    for i in range(0,len(N)-1):
      for j in range(i+1,len(N)):
        target = -1*(N[i]+N[j])
        if target in P:
          result.add(tuple(sorted([N[i],N[j],target])))

    return list(result)
  def main(self, nums:list[int]) -> list[list[int]]:
    result = set()
    for i in range(0,len(nums)-1):
      unique = {}
      for j in range(i+1,len(nums)):
        target = -1 * (nums[i] + nums[j])
        if target in unique:
          # print([sorted((-target,nums[i],nums[j]))])
          result.add(tuple(sorted([target,nums[i],nums[j]])))
        else:
          unique[nums[j]] = True
        # print(nums[i],nums[j],unique," <=> " ,result,-target in unique)
    # print(unique," <-0-> " ,result)
    print(unique)
    return result
