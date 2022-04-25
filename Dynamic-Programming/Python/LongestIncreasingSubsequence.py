def longestIncreasingSubsequence(nums):
    d = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                d[i] = max(d[i], d[j] + 1)
    return max(d)


def lIS(nums):
    d = [1] * len(nums)
    p = [-1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and d[i] < d[j] + 1:
                d[i] = d[j] + 1
                p[i] = j
    output = d[0]
    pos = 0
    for i in range(len(d)):
        if d[i] > output:
            output = d[i]
            pos = i

    sub = []
    while pos != -1:
        sub.append(nums[pos])
        pos = p[pos]
    sub.reverse()
    return sub


def lISDP(nums):
    d = [float("inf")] * len(nums)
    d[0] = float("-inf")
    for i in range(len(nums)):
        for j in range(len(nums)):
            if d[j - 1] < nums[i] and nums[i] < d[j]:
                d[j] = nums[i]
    ans = 0
    for i in range(len(d)):
        if d[i] < float("inf"):
            ans = i
    return ans


def lISBS(nums):
    d = [float("inf")] * (len(nums) + 1)
    d[0] = float("-inf")
    for i in range(len(nums)):
        low, high = 0, len(d) - 1
        while low < high:
            mid = (low + high) >> 1
            if d[mid] < nums[i]:
                low = mid + 1
            else:
                high = mid

        d[low] = nums[i]

    ans = 0
    for i in range(len(d)):
        if d[i] < float("inf"):
            ans = i
    return ans


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(lISBS(nums))


main()
