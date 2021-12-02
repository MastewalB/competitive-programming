"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
"""


def remove_element(nums, val):
    last_val = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[last_val] = nums[i]
            last_val += 1

    print(nums)
    return last_val


nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(remove_element(nums, 2))
