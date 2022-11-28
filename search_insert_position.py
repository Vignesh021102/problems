

#linearSearch
def check(nums,target):
    for i,val in enumerate(nums):
        if target <= val:
            return i
    return len(nums)
import math
def check2(nums,target):
    f = 0
    l = len(nums)-1
    while (f<l) &(f != l-1):
        mid = round((l-f)/2)+f
        print(f,l,mid,nums[mid])
        if nums[mid] > target:
            l = mid
        elif nums[mid] < target:
            f = mid
        else:
            return mid
    #print(f,l,mid)
    if f == l-1:
            if nums[l] == target:
                return l
            elif nums[l] < target:
                return l+1
    return f+1 if nums[f]<target else f


array = [1]
key = 2
#print(check(array,key))
print(check2(array,key))