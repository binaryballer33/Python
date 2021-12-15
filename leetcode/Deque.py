# Just like a Queue except you can add elements to either the front or the back of the Queue


class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        print(self.items[0])
        self.items.remove(self.items[0])

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def getQueue(self):
        return self.items


queue = Deque()
print(f"Size of the Queue is: {queue.size()}")
print(f"Is the Queue Empty: {queue.isEmpty()}")
queue.addFront(1)
queue.addRear(2)
queue.addFront('three')
print(queue.getQueue())
queue.removeFront()
print(queue.getQueue())
print(queue.removeRear())
print(queue.getQueue())