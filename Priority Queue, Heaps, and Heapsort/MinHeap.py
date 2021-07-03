import sys


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def left(self, pos):
        return 2 * pos

    def right(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        largest = pos
        if not self.isLeaf(pos):
            if self.Heap[pos] > self.Heap[self.left(pos)]:
                largest = self.left(pos)

            if self.Heap[pos] > self.Heap[self.right(pos)]:
                largest = self.right(pos)

            if largest != pos:
                self.swap(largest, pos)
                self.minHeapify(largest)

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : " + str(self.Heap[i])+" LEFT CHILD : " +
                  str(self.Heap[2 * i])+" RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    def minHeap(self):

        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def remove(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped