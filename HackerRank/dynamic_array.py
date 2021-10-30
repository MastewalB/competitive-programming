def dynamicArray(n, queries):
    array = [[] for i in range(n)]
    answers = []
    last_answer = 0
    for query in queries:
        x = query[1]
        y = query[2]
        if query[0] == 1:
            index = (x ^ last_answer) % n
            array[index].append(y)
        elif query[0] == 2:
            index = (x ^ last_answer) % n
            second_index = y % len(array[index])
            last_answer = array[index][second_index]
            answers.append(last_answer)
    print(answers)
    return answers


# if __name__ == '__main__':

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     q = int(first_multiple_input[1])

#     queries = []

#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))

n = 2
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
result = dynamicArray(n, queries)
