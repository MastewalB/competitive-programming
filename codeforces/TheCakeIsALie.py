from functools import lru_cache


def cakeM(n, m, k):
    return "YES" if (n * m) - 1 == k else "NO"


def cake(n, m, k):

    @lru_cache(None)
    def cakeLie(x, y, k):
        nonlocal n, m

        if x == n and y == m and k == 0:
            return True
        elif x > n or y > m:
            return False
        elif k <= 0:
            return False
        else:
            return cakeLie(x, y + 1, k - x) or cakeLie(x + 1, y, k - y)

    return "YES" if cakeLie(1, 1, k) else "NO"


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = list(map(int, input().split()))
        print(cakeM(n, m, k))


if __name__ == "__main__":
    main()
