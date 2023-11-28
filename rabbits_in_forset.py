# https://leetcode.com/problems/rabbits-in-forest/description/
def numRabbits(answers: list[int]) -> int:
  obj = {}
  for i in answers:
    if i not in obj:
      obj[i] = 1
    else:
      obj[i] += 1
  print(obj)
  sum = 0
  for i in list(obj.keys()):
    if obj[i] > i:
      sum += obj[i] 
    else:
      sum += obj[i] * i
    print(sum)
  return sum
print(numRabbits([1,1,2]))