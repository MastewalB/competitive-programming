class InPlaceHeap:

    def __init__(self, array):
        self.length = len(array)
        self.heap_size = 0

    @staticmethod
    def parent(pos):
        return pos // 2

    @staticmethod
    def left(pos):
        return 2 * pos

    @staticmethod
    def right(pos):
        return (2 * pos) + 1

    @staticmethod
    def maxHeapify(array, pos):
        length = len(array)
        largest = pos
        left = InPlaceHeap.left(pos)
        right = InPlaceHeap.right(pos)

        if left < length and array[pos] < array[left]:
            largest = left

        if right < length and array[largest] < array[right]:
            largest = right

        if largest != pos:
            array[pos], array[largest] = array[largest], array[pos]
            InPlaceHeap.maxHeapify(array, largest)

    def build_max_heap(array):
        for i in range(len(array) - 1, -1, -1):
            InPlaceHeap.maxHeapify(array, i)


array = [2, 7, 4, 1, 8, 1]
InPlaceHeap.build_max_heap(array)
print(array)
