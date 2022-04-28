import sys
input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return (list(map(int, input().split())))


def min_coin(a, b):
    if a == 0 and b > 0:
        return 1
    if a > 0 and b == 0:
        return a + 1

    return (2 * b) + a + 1


def main():
    n = inp()
    for _ in range(n):
        a, b = inlt()
        print(min_coin(a, b))


if __name__ == "__main__":
    main()
