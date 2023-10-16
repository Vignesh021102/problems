import re
# def longestPalindrom(s):
# 	if len(s) == 1:
# 		return s
# 	longArr = []
# 	for i in range(len(s)):
# 		for j in range(i,len(s)+1):
# 			temp = s[i:j+1]
# 			Bool = False
# 			for k in range(len(temp)//2):
# 				# print(temp[k],temp[(-1 * k) - 1],temp[k] != temp[(-1 * k) - 1], temp)
# 				if temp[k] != temp[(-1 * k) - 1]:
# 					#not a palindrom
# 					Bool = True
# 			# print(Bool,temp,i,j,len(s))
# 			if not Bool and len(longArr) <= len(temp):
# 				longArr = temp
# 		# print("  ")
# 	print(longArr)
# 	return longArr
def longestPalindrom(s):
	arr = ""
	longArr = ""
	for i in s:
		# print(i)
		if i in arr: 
			arr = arr + i
			print(re.findall(f"{i}[\w*]{i}",s),i)
			temp = arr[arr.index(i):]
			print("tmep = ",temp)
			Bool = False
			for k in range(len(temp)//2):
				if temp[k] != temp[(-1 * k) - 1]:
					Bool = True
			if not Bool and len(longArr) <= len(temp):
				longArr = temp
		else:
			arr = arr + i

	print(arr[0] if longArr == "" else longArr)
	return arr[0] if longArr == "" else longArr
# longestPalindrom("cabaca")
# longestPalindrom("ca")
longestPalindrom("aacabdkacaa")
