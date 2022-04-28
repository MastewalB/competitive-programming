t = int(input())

for _ in range(t):
    div = int(input())
    if div >= 1900:
        print("Division 1")
    elif 1600 <= div <= 1899:
        print("Division 2")
    elif 1400 <= div <= 1599:
        print("Division 3")
    else:
        print("Division 4")
