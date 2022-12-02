# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

def closeStrings(word1: str, word2: str) -> bool:
    obj1 = {}
    obj2 = {}
    x = 0
    while(x<len(word1))&(x<len(word2)):
        try:
            obj1[word1[x]]+=1
        except:
            obj1[word1[x]] = 1
        try:
            obj2[word2[x]]+=1
        except:
            obj2[word2[x]] = 1
        x+=1
    for i in range(x,len(word1)):
        try:
            obj1[word1[i]]+=1
        except:
            obj1[word1[i]] = 1
    for i in range(x,len(word2)):
        try:
            obj2[word2[i]]+=1
        except:
            obj2[word2[i]] = 1
    obj1Len = len(obj1)
    obj2Len = len(obj2)
    #print(obj1Len,obj2Len)
    if obj1Len!= obj2Len:
        return False
    isSecond = False

    arr1 = list(obj1.keys())
    arr2 = list(obj2.keys())

    for i in arr1:
        if i not in arr2:
            if isSecond:
                return False
            else:
                if len(arr1) == 1:
                    return False
                isSecond = True


    arr1 = list(obj1.values())
    arr2 = list(obj2.values())

    for i in arr1:
        j = 0
        while j < obj2Len:
            if i  == arr2[j]:
                del arr2[j]
                obj2Len-=1
                break
            else:
                j+=1
    if(obj2Len>0):
        return False
    return True

print(closeStrings('abca','ebce'))