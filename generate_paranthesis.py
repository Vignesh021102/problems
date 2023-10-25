import numpy as np
def generate(n):
	arr = {}
	if n == 1:
		return ["()"]
	def create(s,i = 0,m = 1):
		si = s[0:i+1]+"()"+s[i+1:]
		so = s[0:i]+"()"+s[i:]
		# print(si," <=> ",so)
		if m == n-1:
			try:
				arr[si] += 1
			except:
				arr[si] = 0
			try:
				arr[so] += 1
			except:
				arr[so] = 0
		elif m < n-1:
			create(si,i+1,m+1)
			create(so,i+1,m+1)
			create(so,i+3,m+1)
		return 
	create("()")
	print(arr)
	print(list(arr.keys()))
	return list(arr.keys())
result = generate(8)