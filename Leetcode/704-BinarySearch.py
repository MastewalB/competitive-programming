import math


def binary_search(nums, target):

    begin, end = 0, len(nums) - 1

    while begin <= end:
        pivot = math.floor((end - begin) // 2) + begin

        if nums[pivot] == target:
            return pivot

        if target < nums[pivot]:
            end = pivot - 1

        else:
            begin = pivot + 1

    return -1


nums = [-1, 0, 3, 5, 9, 14, 12]
nums = [2, 5]
nums = [-1, 0, 5]
print(binary_search(nums, -1))
