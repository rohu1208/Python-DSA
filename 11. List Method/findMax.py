# n=len(my_list)
# maxi=0
# for i in range(0,n):


# def findMax(nums: list) -> int:
#     n = len(nums)
#     maxi = 0
#     for i in range(0, n):
#         if nums[i] > maxi:
#             maxi = nums[i]
#     return maxi


# my_list = [45, 23, 56, 78, 95, 21, 245, 89, 32, 1, 3, 5, 6]
# print(findMax(my_list))


# for negative
# def findMax(nums: list) -> int:
#     n = len(nums)
#     maxi = float("-inf")
#     for i in range(0, n):
#         if nums[i] > maxi:
#             maxi = nums[i]
#     return maxi


# my_list = [45, 23, 56, -78, 95, 21, 245, 89, 32, 1, 3, 5, 6]
# print(findMax(my_list))


def findMax(nums: list) -> int:
    n = len(nums)
    maxi = float("-inf")
    for i in range(0, n):  # O(n)
        maxi = max(maxi, nums[i])  # O(1)
    return maxi


my_list = [45, 23, 56, 78, 95, 21, 245, 89, 32, 1, 3, 5, 6]
print(findMax(my_list))
