class InPlaceHeap:
    heap_size = 0

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

        heap_size = InPlaceHeap.heap_size
        largest = pos
        left = InPlaceHeap.left(pos)
        right = InPlaceHeap.right(pos)

        if left < heap_size and array[pos] < array[left]:
            largest = left

        if right < heap_size and array[largest] < array[right]:
            largest = right

        if largest != pos:
            array[pos], array[largest] = array[largest], array[pos]
            InPlaceHeap.maxHeapify(array, largest)

    @staticmethod
    def minHeapify(array, pos):

        heap_size = InPlaceHeap.heap_size
        smallest = pos
        left = InPlaceHeap.left(pos)
        right = InPlaceHeap.right(pos)

        if left < heap_size and array[pos] > array[left]:
            smallest = left

        if right < heap_size and array[smallest] > array[right]:
            smallest = right

        if smallest != pos:
            array[pos], array[smallest] = array[smallest], array[pos]
            InPlaceHeap.minHeapify(array, smallest)

    def build_heap(array, rule):
        InPlaceHeap.heap_size = len(array)
        for i in range(len(array) - 1, -1, -1):
            InPlaceHeap.maxHeapify(
                array, i) if rule > 0 else InPlaceHeap.minHeapify(array, i)


""" array = [2, 7, 4, 1, 8, 1]
InPlaceHeap.build_heap(array, 0)
print(array) """
