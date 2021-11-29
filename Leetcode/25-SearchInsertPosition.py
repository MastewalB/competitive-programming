"""Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""
import math


def searchInsert(nums, target):
    if len(nums) == 0:
        return 0
    begin, end = 0, len(nums) - 1

    while(begin <= end):
        pivot = math.floor((end - begin) // 2) + begin

        if nums[pivot] == target:
            return pivot

        if target < nums[pivot]:
            end = pivot - 1

        else:
            begin = pivot + 1

    return pivot if nums[pivot] > target else pivot + 1


nums = [1, 3, 5, 6]
#nums = []
print(searchInsert(nums, 7))
