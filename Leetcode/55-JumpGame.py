array = [3, 2, 1, 0, 4]
array = [1]
#array = [0]
#array = [2, 3, 1, 1, 4]


def can_jump(array):
    current_index = 0
    last_index = len(array) - 1

    while current_index <= len(array):
        if current_index + array[current_index - 1] == current_index:
            if current_index + array[current_index - 1] == len(array):
                return True
            return False
        elif current_index + array[current_index - 1] == len(array):
            return True
        else:
            current_index += array[current_index - 1]


print(can_jump(array))
