#implementaion of merger sort




def merge_sort(arr):
    import math
    #merger func merges the splited arrays in asc order
    def merger(upperArr,lowerArr):
        i = 0
        j = 0
        arr = []
        #print(upperArr,lowerArr)
        while (i < len(upperArr)) & (j < len(lowerArr)):
            if upperArr[i] < lowerArr[j]:
                arr.append(upperArr[i])
                i+=1
            else:
                arr.append(lowerArr[j])
                j+=1
        arr = arr+upperArr[i:]+lowerArr[j:]
        #print(f"arr = {arr}")
        return arr
    #spliter func splits the arrays in half and calls merger func (in recursive order)
    def spliter(splitArr):
        mid = math.floor(len(splitArr)/2)
        #print(splitArr)
        if len(splitArr) == 2:
            splitArr = merger([splitArr[0]],[splitArr[1]])
        else:
            upper = spliter(splitArr[0:mid])
            lower = spliter(splitArr[mid:])
            splitArr = merger(upper,lower)
        return splitArr
    print(spliter(arr))
    
merge_sort([1,13,2,7,6,5,0,9])