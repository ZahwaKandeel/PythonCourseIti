from Day05.queueClass import Queue
import json


class QueueOutOfRangeException(Exception):
    pass

class childQueue(Queue):
    queues = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size

        childQueue.queues[name] = self

    def insert(self, item):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException

        super().insert(item)

    @classmethod
    def get_queue(cls, name):
        return cls.queues[name]

    @classmethod
    def save(cls):
        data = {}
        for name, queue in cls.queues.items():
            data[name] = {
                "size": queue.size,
                "items": queue.items
            }
        with open("queues.json", "w") as f:
            json.dump(data, f)

    @classmethod
    def load(cls):
        try:
            with open("queues.json", "r") as f:
                data = json.load(f)
            for name, info in data.items():
                q = childQueue(name, info["size"])
                q.items = info["items"]
        except:
            print("No saved data found")


q1 = childQueue("q1", 3)
q1.insert(40)
q1.insert(50)
q1.insert(60)
#q1.insert(70)   #test queue out of range exception
print(q1.items)

q2 = childQueue("q2", 2)
q2.insert(90)
print(q2.items)

test1 = childQueue("A", 3)
test2 = childQueue("B", 5)

print(childQueue.get_queue("A") is test1)
print(childQueue.get_queue("A") is test2)

childQueue.save()
childQueue.load()