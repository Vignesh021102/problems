def check(string1, string2):
  obj1 = {}
  obj2 = {}
  for i in string1:
    try:
      obj1[i] += 1
    except:
      obj1[i] = 1
  for i in string2:
    try:
      obj2[i] += 1
    except:
      obj2[i] = 1
  # print(obj1,obj2)
  return obj1 == obj2 
print(check("ratr","tar"))