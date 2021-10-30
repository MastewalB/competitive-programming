def matchingStrings(strings, queries):
    results = []
    for query in queries:
        result = 0
        for string in strings:
            if query == string:
                result += 1
        results.append(result)

    print(results)


if __name__ == '__main__':

    # strings_count = int(input().strip())

    # strings = []

    # for _ in range(strings_count):
    #     strings_item = input()
    #     strings.append(strings_item)

    # queries_count = int(input().strip())

    # queries = []

    # for _ in range(queries_count):
    #     queries_item = input()
    #     queries.append(queries_item)

    strings = ['aba', 'baba', 'aba', 'xzxb']
    queries = ['aba', 'xzxb', 'ab']

    res = matchingStrings(strings, queries)
