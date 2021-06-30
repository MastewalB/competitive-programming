k = 15

t = 2
while k != 1:
    if k % t == 0:
        k /= t
        print(t)
    else:
        if t * t > k:
            t = k
        else:
            t += 1
