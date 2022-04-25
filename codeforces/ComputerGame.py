def computerGame(grid):
    output = False

    for i in range(len(grid[0])):
        output |= grid[0][i] == '1' and grid[1][i] == '1'
    if not output:
        return "YES"
    return "NO"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for _ in range(2):
            arr.append(list(input()))
        print(computerGame(arr))


if __name__ == "__main__":
    main()
