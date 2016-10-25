from node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def remove(self, item):
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
        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.get_next()
        return current.get_data()

    def pop(self, index=None):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.get_next()
        if index is None:
            index = size - 1
        current_node = self.head
        previous_node = None
        count = 0
        while count < index:
            count += 1
            previous_node = current_node
            current_node = current_node.get_next()

        deleted_node = current_node

        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

        return deleted_node.get_data()

# Could add an Iterator class like in the wikibooks example of linked lists, since utilizes code reusability.
