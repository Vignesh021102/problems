# https://leetcode.com/problems/longest-valid-parentheses/description/
def longestValidParentheses(s):
	if len(s) == 0:
		return 0
	stack = [s[0]]
	iStack = [0]
	obj = {"(":")",")":"("}
	res = [False for _ in range(len(s))]
	for i in range(1,len(s)):
		if stack:
			if stack[-1] == obj[s[i]]:
				res[i] = True
				res[iStack[-1]] = True
				stack = stack[:-1]
				iStack = iStack[:-1]
				#True
			else:
				stack.append(s[i])
				iStack.append(i)
		else:
			stack.append(s[i])
			iStack.append(i)
	Max = 0
	Max2 = 0
	# print(res)
	for i in range(len(res)):
		if res[i]: 
			Max2 += 1
		else:
			if Max2 > Max:
				Max = Max2
				Max2 = 0
	return Max if Max  else Max2
print(longestValidParentheses(")()()))"))