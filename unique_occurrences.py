# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.


def check(arr):
    obj = {}
    for val in arr:
        try:
            obj[val] += 1
        except:
            obj[val] = 1
    #print(obj)
    return True if len(set(obj.values())) == len(obj) else False

print(check([1,2,1,3])) 
