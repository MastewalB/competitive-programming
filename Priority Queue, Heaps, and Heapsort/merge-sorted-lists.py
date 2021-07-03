from MinHeap import MinHeap

lists = [[1, 4, 5], [1, 3, 4], [2, 6, 7]]
total_len = 0
max_len = 0
for i in lists:
    if len(i) > max_len:
        max_len = len(i)
    total_len += len(i)


heap = MinHeap(total_len)
for i in range(max_len):
    for j in range(len(lists)):
        if i < len(lists[j]):

            heap.insert(lists[j][i])

heap.Print()
