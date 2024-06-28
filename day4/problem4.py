# Given an array of integers, find the first missing positive integer in
# linear time and constant space. In other words, find the lowest positive integer
# that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# first way
nums = [3, 4, -1, 1]


def first_mising_number():
    for i, t in enumerate(nums, 1):
        if i not in nums:
            return i
    return max(nums)+1


print(first_mising_number())
# second_way
# def first_mising_number():
#     global nums
#     if not nums:
#         return 1
#     for i, num in enumerate(nums):
#         while i + 1 != nums[i] and 0< nums[i]<=len(nums):
#             v = nums[i]
#             nums[i], nums[v -1] = nums[v -1], nums[i]
#             if nums[i] == nums[v -1]:
#                 break
#
#     for i, num in enumerate(nums, 1):
#         if i not in nums:
#             return i
#     return len(nums) +1
#
#
# print(first_mising_number())