import sys


def promising_string(string):
    promising = 0

    for i in range(len(string)):
        plus, minus, adjacent, prev, prev_count = 0, 0, 0, " ", 0
        for j in range(i, len(string)):
            if string[j] == "-":
                minus += 1
                if prev == string[j]:
                    prev_count += 1
                else:
                    prev_count = 1

            else:
                plus += 1
                adjacent += (prev_count // 2)
                prev_count = 0
            if minus == plus:
                print(i, j)
                promising += 1
            elif minus > plus and (minus - plus) % 3 == 0 and adjacent + (prev_count // 2) >= (minus - plus) // 3:
                print(i, j)
                promising += 1
            prev = string[j]
    return promising


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        an = int(input())
        string = input()
        print(promising_string(string))
