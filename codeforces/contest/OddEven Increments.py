

def increment(arr):
    if len(arr) == 1:
        return "YES"
    odds = 1 if arr[1] % 2 == 0 else 0
    evens = 1 if arr[0] % 2 == 0 else 0

    for i in range(len(arr)):
        if i % 2 == 0:
            if (arr[i] % 2 == 0) != evens:
                return "NO"
        else:
            if (arr[i] % 2 == 0) != odds:
                return "NO"
    return "YES"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(increment(arr))


if __name__ == "__main__":
    main()
