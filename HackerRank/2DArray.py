
array = [[-9, -9, -9,  1, 1, 1],
         [0, -9,  0,  4, 3, 2],
         [-9, -9, -9,  1, 2, 3],
         [0,  0,  8,  6, 6, 0],
         [0,  0,  0, -2, 0, 0],
         [0,  0,  1,  2, 4, 0]]

new_array = [[], [], [], []]

length = len(array) - 1

for i in range(length):
    if length - i >= 2:

        for j in range(len(array[i])):
            if len(array[i]) - 1 - j >= 2:
                level_sum = 0

                for k in range(j, j+3):

                    level_sum += array[i][k] + array[i+2][k]
                    if k == j+1:
                        level_sum += array[i+1][k]

                new_array[i].append(level_sum)


def ret_max(td_array):
    max_sum = td_array[0][0]
    for i in range(len(td_array)):
        for j in range(len(td_array[i])):
            max_sum = max(td_array[i][j], max_sum)

    return max_sum
    # return max


ret_max(new_array)
