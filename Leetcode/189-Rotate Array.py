"""Rotation through reversing"""


def reverse(nums, begin, end):
    while begin < end:
        nums[begin], nums[end] = nums[end], nums[begin]
        begin += 1
        end -= 1


def rotate(nums, k):

    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

    print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
