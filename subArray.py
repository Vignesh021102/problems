def check(arr,num):
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      if sum(arr[i:j+1]) == num:
        print(arr[i:j+1])
        try:
          count+=1
        except:
          count = 1
  print(count)
  return count
check([1,13,22,23,45],45)