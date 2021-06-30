k = 15

while k != 1:
    t = 2
    while k % t != 0:
        t += 1
    print(t)

    k /= t


t = 2
while k != 1:
    if k % t == 0:
        k /= t
        print(t)
    else:
        t += 1
