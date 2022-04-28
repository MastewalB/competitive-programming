

def triple(arr):
    count = [0] * (len(arr) + 1)
    # print(count)
    for i in arr:
        count[i] += 1
        if count[i] == 3:
            return i
    return -1


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(triple(arr))


if __name__ == "__main__":
    main()
