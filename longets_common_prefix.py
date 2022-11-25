# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


x = ["car","cab","ctt"]
def check(x):
    letterNum = 0
    letter = ''
    string = ''
    while(True):
        if letterNum >= len(x[0]):
            return string
        letter = x[0][letterNum]
        Boo = True
        for i in range(1,len(x)):
            if letterNum >= len(x[i]):
                return string
            if letter != x[i][letterNum]:
                Boo = False
        if Boo:
            string+=letter
        else:
            return string
        letterNum+=1
        
print(check(x))