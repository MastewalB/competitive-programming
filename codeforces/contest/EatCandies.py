
def candies(arr):
    if len(arr) == 1:
        return 0
    alice, left = 0, -1
    bob, right = 0, len(arr)
    last_count = count = 0

    while left < right:
        if alice == bob:
            left += 1
            right -= 1
            last_count = count
            alice += arr[left]
            bob += arr[right]
            count += 2

        if alice < bob:
            while alice < bob and left < right:
                left += 1
                alice += arr[left]
                count += 1
        elif alice > bob:
            while bob < alice and left < right:
                right -= 1
                bob += arr[right]
                count += 1

    return last_count


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(candies(arr))


if __name__ == "__main__":
    main()
