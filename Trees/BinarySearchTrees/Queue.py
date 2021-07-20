class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        answer = self.queue[0]

        self.queue.pop(0)
        return answer

    def peek(self):

        if self.isEmpty():
            return "Empty"
        else:
            print(self.queue[0])

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.size() == 0

    def clear(self):

        self.queue = []
