# https://leetcode.com/problems/k-th-symbol-in-grammar/description
#trial one (string generation)
def kthGrammar( n: int, k: int) -> int:
  obj = {"1":"0","0":"1"}
  def inverse(s):
    if s == "0":
      return "1"
    return s[int(len(s)/2):] + s[0:int(len(s)/2)]
    # return "".join([obj[s[i]] for i in range(len(s))])
  temp = ""
  def create(n:int ) -> str:
    if n == 1:
      return "0"
    temp = create(n-1)
    return temp+inverse(temp)
  res = create(n)
  return res

#trial two guess without string generation!!!
def guess(n:int, k:int) -> int:
  inverse = False
  for i in range(n,1,-1):
      mid = int((2 ** (i -1))/2)
      if k > mid:
          k -= mid
          inverse = True^inverse
  return 1 if inverse else 0
# print(kthGrammar(30,1))
# for i in range(1,16):
#   print(guess(5,i)) 
# print(kthGrammar(1,1))