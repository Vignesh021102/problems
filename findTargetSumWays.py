def findTargetSumWays(nums: list[int], target: int)-> int:
	# print(nums,target)
	result = []
	temp = []
	count = 0
	for index, element in enumerate(nums):
		temp = []
		if result == []:
			temp = [element,-element]
			if index == len(nums)-1:
				if element == target:
					count+=1
				if -element == target:
					count+=1
		else:
			for j in result:
				if index == len(nums)-1:
					print(j,element,[j+element, j-element])
					if j+element == target:
						count+=1
					if j-element == target:
						count+=1
				else:
					temp += [j+element, j-element]
		result = temp
		print(element)
		print(temp)
	return count

# print(findTargetSumWays([1,1,1,1,1],3))
print(findTargetSumWays([1,0],1))