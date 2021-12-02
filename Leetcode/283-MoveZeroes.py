def moveZeroes(nums):
    zero = len(nums)
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 0:
            if i < zero:
                for j in range(i + 1, len(nums)):
                    nums[j - 1] = nums[j]
                nums[len(nums) - 1] = 0
                zero -= 1
                i = i - 1
            else:
                break
        i += 1


def movezeroespt(nums):
    last_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
        print(nums)
        print(last_non_zero)

    for j in range(last_non_zero, len(nums)):
        nums[j] = 0


nums = [0, 1, 0, 3, 12]
nums = [0, 0, 0]
nums = [1, 2]
movezeroespt(nums)
print(nums)
