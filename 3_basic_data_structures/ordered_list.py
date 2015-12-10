from node import Node


class OrderedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        pass

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, item):
        pass

    def remove(self):
        current_node = self.head
        previous_node = None
        found = False
        while not found:
            if current_node.get_data() == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

    def index(self, index):
        pass

    def append(self, item):
        pass

    def insert(self, index, item):
        pass

    def pop(self, index=None):
        pass