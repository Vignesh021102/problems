# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory



# algorithm
#     if dup{duplicate} == -1 check for first duplicate
#     if dup != -1 then compare each element with element in dup-1 index if both element not equal (unique element is found) so swap pos of dup and current element and dup = dup+1


def remove_duplicate(nums):
    dup = 1
    for i in range(1,len(nums)):
        if dup == -1:
            if nums[i] == nums[i-1]:
                #nums[i] is first duplicate
                dup = i
        else:
            if nums[i] != nums[dup-1]:
                #moving the duplicate to one index right
                nums[dup] = nums[i] 
                dup+=1
    return len(nums) if dup == -1 else dup


array = [0,0,1,1,2,3]
print(f' result = {remove_duplicate(array)}')
print(array)