def rotateLeft(d, arr):
    length = len(arr)
    new_arr = []
    if d > length:
        d = d % length

    for i in range(len(arr)):
        next_element_index = (i + d) % length
        new_arr.append(arr[next_element_index])
    return new_arr


if __name__ == '__main__':

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # d = int(first_multiple_input[1])

    # arr = list(map(int, input().rstrip().split()))

    d = 4
    arr = [1, 2, 3, 4, 5]
    result = rotateLeft(d, arr)
