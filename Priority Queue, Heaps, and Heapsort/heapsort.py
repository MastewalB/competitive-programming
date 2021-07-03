from MinHeap import MinHeap


array = [1, 2, 3, 21, 1, 1, 2]
heap = MinHeap(len(array))
for i in array:
    heap.insert(i)


for i in range(1, len(array)):
    array[i - 1] = heap.remove()
    heap.Print()
print(array)
