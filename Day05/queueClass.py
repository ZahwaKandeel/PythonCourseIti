class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items.pop(0)

    def is_empty(self):
        if len(self.items) == 0 :
            return True
        return False