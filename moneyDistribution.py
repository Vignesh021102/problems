# https://leetcode.com/problems/distribute-money-to-maximum-children/description/
def distMoney(money: int, children: int):
	print(money,children)
	if money <= 0 and children <= 0:
		return 0
	if children == 1:
		return 1 if money == 8 else 0
	elif money >= children:
		if (money - 8) >= (children - 1) and (money - 8) != 4:
			return 1 + distMoney(money-8,children-1)
		else:
			return distMoney(money-1,children-1)
	else:
		return -1

def distMoney(money: int, children: int):
	print(money,children)
	if money == children:
		return 0
	elif money < children:
		return -1
	elif money > 8:
		res = int(money/8)
		print(money%8 != 4 , (res) , (money%8 ))
		return res if (not (money%8 == 4 and (children - res) == 1)) and (res == children or money%8 >= (children - res )) else res - 1
	else:
		return 0
print(distMoney(16,1))