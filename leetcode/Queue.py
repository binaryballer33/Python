# Queues operate on a First In First Out(FIFO)
# Enqueue is when you add to the beginning of the Queue
# Dequeue is when you remove the first element of the Queue


class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def getQueue(self):
        return self.items


queue = Queue()
print(f"Size of the Queue is: {queue.size()}")
print(f"Is the Queue Empty: {queue.isEmpty()}")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue('three')
print(queue.getQueue())
print(queue.dequeue())
print(queue.getQueue())
print(queue.dequeue())
print(queue.getQueue())

