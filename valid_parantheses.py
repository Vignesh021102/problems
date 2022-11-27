# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false




string = ')'

def check(string:str)->bool:
    #print(string)
    closing = [')',']','}']
    matchingsym = {')':'(',']':'[','}':'{'}
    stack = []
    i = 0
    while i < len(string):
        if string[i] in closing:
            if len(stack) == 0:
                return False
            if(stack.pop() != matchingsym[string[i]]):
                return False
        else:
            stack.append(string[i])
        i+=1
    return False if len(stack)> 0 else True
print(f'{string} = {check(string)}')
print(check.__annotations__)