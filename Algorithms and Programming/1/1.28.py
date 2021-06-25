n = 10

a = 1
s = 0

while a * a < n:
    b = 1
    t = 0
    while a * a + b * b < n:
        b += 1
        t += 1
    a += 1
    s += t

print(s)
