# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/
import numpy as np
def equalFrequency(s):
	obj = {}
	for i in s:
		if i in obj:
			obj[i] += 1
		else:
			obj[i] = 1
	temp = {}
	for i in obj.values():
		if i in temp:
			temp[i] += 1
		else:
			temp[i] = 1
	mode = list(temp.keys())[list(temp.values()).index(max(temp.values()))]
	res = 0
	for i in obj.values():
		res -= (i - mode)
	print(res)
	print(obj)
	return res

print(equalFrequency("bxxxvvvaaaaa"))