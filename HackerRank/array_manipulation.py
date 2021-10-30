def array_manipulation(n, queries):
    array = [0 for i in range(n)]
    max_val = 0
    for i in range(len(queries)):
        for k in range(queries[i][0] - 1, queries[i][1]):
            array[k] += queries[i][2]
            if array[k] > max_val:
                max_val = array[k]
        print(array)
    return max_val


if __name__ == '__main__':

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # queries = []

    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))

    n = 10
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    #queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]

    result = array_manipulation(n, queries)
    print(result)
