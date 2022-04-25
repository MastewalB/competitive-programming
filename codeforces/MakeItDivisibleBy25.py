def divisible(num, sub):
    count = 0
    j = len(num) - 1
    while j >= 0 and num[j] != sub[1]:
        count += 1
        j -= 1
    if j < 0:
        return float("inf")
    j -= 1
    while j >= 0 and num[j] != sub[0]:
        count += 1
        j -= 1
    return count if j >= 0 else float("inf")


def main():
    subsequs = ["00", "25", "50", "75"]
    t = int(input())
    for _ in range(t):
        ans = float("inf")
        num = input()
        for sub in subsequs:
            ans = min(ans, divisible(num, sub))
        print(ans)


if __name__ == "__main__":
    main()
