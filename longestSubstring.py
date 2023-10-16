def longestString(s):
	stack = []
	longStack = []
	lenStack = len(stack)
	lenLongStack = len(longStack)
	for i in s:
		lenStack = len(stack)
		lenLongStack = len(longStack)
		# print(stack,longStack)
		try:
			# print(stack[-1] != i and i not in stack, stack ,i,"  ",longStack)
			if stack[-1] != i and i not in stack:
				stack.append(i)
			else:
				# print(stack,longStack,lenStack > lenLongStack)
				if lenStack > lenLongStack:
					longStack = stack
				try:
					stack = stack[stack.index(i)+1:]
					stack.append(i)
				except:
					stack = [i]
		except:
			stack.append(i)
	
	if len(stack) >= len(longStack):
		longStack = stack
	return len(longStack)
print(longestString("cdd"))