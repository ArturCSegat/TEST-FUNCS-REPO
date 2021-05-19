arr1 = [1, 3, 5, 6]
target1 = 8

def twoSum(arr, target):
    values = dict()

    for i, elem in enumerate(arr):
        comp = target - elem

        if comp in values:
            return [values[comp], i]
        
        values[elem] = i

    return []

#print(twoSum(arr1, target1))

arr2 = [2, 4, 3, 5, 2, 10, 29, 2, 4]
def findDuplicate(nums):
    dups = []
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            dups.append(nums[i])
    return dups
    
# print(findDuplicate(arr2))

arr3 = [1, 2, 0]
arr4 = [3,4,-1,1]
#THIS ALSO DOES NOT WORK
# def findMissingPossitive(nums):
#     nums.sort()
#     for i in nums:
#         if nums[i] == len(nums)-1:
#             return i+1
#         if nums[i+1] != i+1 and i > 0:
#             return i+1

# -1 1 3 4

#print(findMissingPossitive([])) 

#THIS DOES NOT WORK
# arr5 = [4,1,2,1,2]
# def singleNumber(nums):
#         nums.sort()
#         dups = []
#         for i in nums:
#             if nums[i] == nums[i-1]:
#                 dups.append(nums[i])
        
#         for i in nums:
#             if i not in dups:
#                 return 

# print(singleNumber(arr5))


print("TEST1")


print("TEST2")
print("TEST2")