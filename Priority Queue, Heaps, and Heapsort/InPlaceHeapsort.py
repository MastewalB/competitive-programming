from InPlaceHeap import InPlaceHeap


class InPlaceHeapSort:

    @staticmethod
    def sort(array):
        InPlaceHeap.build_heap(array, 1)
        print(array)
        for i in range(len(array) - 1, 1, -1):
            array[i], array[0] = array[0], array[i]
            InPlaceHeap.heap_size -= 1
            InPlaceHeap.maxHeapify(array, 0)


array = [2, 7, 4, 1, 8, 1]
InPlaceHeapSort.sort(array)
print(array)
