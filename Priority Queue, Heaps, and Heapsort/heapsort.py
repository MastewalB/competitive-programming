from MinHeap import MinHeap


array = [1, 2, 20, 21, 352, 65, 1, 5, 2]
heap = MinHeap(len(array))
for i in array:
    heap.insert(i)


for i in range(1, len(array) + 1):
    array[i - 1] = heap.remove()

print(array)
