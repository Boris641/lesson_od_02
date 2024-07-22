class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []

    def enqaueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


queue = Queue()

print(queue.is_empty())

queue.enqaueue("Дейсивие 1")
queue.enqaueue("Дейсивие 2")
queue.enqaueue("Дейсивие 3")

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())