# Given an integer x, return true if x is a  palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


x = 1001
def check(x):
    if x <0:
        return False
    string = str(x)
    mid = int(len(string)/2)
    if len(string)%2 == 0:
        mid2 = mid
    else:
        mid2 = mid+1
    return ''.join(list(reversed(string[:mid]))) == string[mid2:]
check(x)#should return true
