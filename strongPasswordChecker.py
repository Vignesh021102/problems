import re
def strongPasswordChecker(password):
	obj = {}
	#char count
	lenPas = len(password)
	count = {"move":0}
	count["add"] = (6 - lenPas) if lenPas < 6 else 0
	count["remove"] = (lenPas - 20) if lenPas  > 20 else 0
	print(count)

	for i in password:
		if i in obj:
			obj[i] += 1
		else:
			obj[i] = 1
	triple = {}
	other = {}
	tempCount = 0
	print(obj,triple,count,tempCount)
	for i in range(0,lenPas-2,3):
		print(i,password[i],tempCount,other)
		if password[i] == password[i+1] == password[i+2]:
			triple[password[i]] = True
			count["move"] += 1
			if password[i] in other:
				if other[password[i]] == 0:
					count["add"] += 1 
					lenPas += 1
				else:
					other[password[i]] -= 1
			elif password[i] not in other:
				other[password[i]] = lenPas - obj[password[i]] - 1
	# if tempCount > count:
	# 	count = tempCount
	# tempCount = 0
	print(obj,triple,count,other)
	if not re.search(r"[A-Z]",password):
		if lenPas < 20:
			count["add"] += 1
		else:
			count["add"] += 1
			if count["remove"] == 0:
				count["remove"] += 1
		lenPas += 1
	if not re.search(r"[a-z]",password):
		if lenPas < 20:
			count["add"] += 1
		else:
			count["add"] += 1
			if count["remove"] == 0:
				count["remove"] += 1
		lenPas += 1
	if not re.search(r"[0-9]",password):
		if lenPas < 20:
			count["add"] += 1
		else:
			count["add"] += 1
			if count["remove"] == 0:
				count["remove"] += 1
		lenPas += 1
	# if tempCount > count:
	# 	count = tempCount
	# print(obj,triple,count)
	print(obj,triple,count,tempCount)
	return count
strongPasswordChecker("Baaabbb")
strongPasswordChecker("1337C0d3")
strongPasswordChecker("aA1")
strongPasswordChecker("ABABABABABABABABABAB1")
strongPasswordChecker("11111111")
strongPasswordChecker("aabaabaacaacaacaacaacac")