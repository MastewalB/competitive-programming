INT_MIN = -32767


def cut_rod(price, length):
    sub_values = [0 for x in range(length + 1)]
    sub_values[0] = 0

    for i in range(1, length + 1):
        max_value = INT_MIN
        for j in range(0, i // 2 + 1):
            max_value = max(max_value, price[j] + price[i - j])
            print(str(i) + " Max value for " + str(j) + " + " +
                  str(i - j) + " = " + str(max_value))
        sub_values[i] = max_value

    return sub_values[length]


price = [0, 1, 5, 8, 9, 10, 17, 17]
print("Maximum Obtainable Value is " + str(cut_rod(price, 5)))
