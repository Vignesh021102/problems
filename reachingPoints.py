# https://leetcode.com/problems/reaching-points/

#incrementing
# def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
#   # sx = 35
#   # sy = 13
#   # tx = 455955547
#   # ty = 420098884
#   # recursion depth reached
#   if sx == tx and sy == ty:
#     return True
#   elif sx >tx or sy > ty:
#     return False
#   return reachingPoints(sx+sy,sy,tx,ty) or reachingPoints(sx,sx+sy,tx,ty)

#decrementing
def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
  # sx = 35
  # sy = 13
  # tx = 455955547
  # ty = 420098884
  # recursion depth reached
  print(sx,sy,tx,ty,ty%sx == 1,tx%sy == 1)
  if sx == tx and sy == ty:
    return True
  elif tx<sx or ty<sx:
    return False
  elif sx == tx:
    return reachingPoints(sx,sx,tx,ty-sx)
  elif sy == ty:
    return reachingPoints(sx,sy,tx-sy,ty)
  return reachingPoints(sx,sy,tx-ty,ty) or reachingPoints(sx,sx,tx,ty-tx)
# print(reachingPoints(35,13,455955547,420098884))
print(reachingPoints(9,10,9,19))
print(reachingPoints(1,1,3,5))