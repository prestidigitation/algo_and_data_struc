from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, item):
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()
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

# Index method has time complexity O(n) since it traverses the list until it reaches the correct index.
    def index(self, index):
        current_node = self.head
        current_index = 0
        while current_index != index:
            current_index += 1
            current_node = current_node.get_next()
        return current_node.get_data()

# Append method has time complexity O(n) since it traverses the entire list to find the last node.
    def append(self, item):
        current_node = self.head
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        new_node = Node(item)
        current_node.set_next(new_node)

# Insert method has time complexity O(n) since it traverses the list until is reaches the correct index.
    def insert(self, index, item):
        current_node = self.head
        current_index = 0
        previous_node = None
        while current_index != index:
            previous_node = current_node
            current_index += 1
            current_node = current_node.get_next()

        if index == 0:
            self.add(item)
        else:
            temp = current_node
            current_node = Node(item)
            current_node.set_next(temp)
            previous_node.set_next(current_node)

# Pop method is O(n) since it must traverse the list to find the correct index.
# Added default index parameter to mimic behavior of regular Python list.pop() method.
# unordered_list.pop() using default index is O(n) since 2n time complexity is still n.
    def pop(self, index=None):
        if index is None:
            index = self.size() - 1

        current_node = self.head
        previous_node = None
        current_index = 0

        while current_index != index:
            current_index += 1
            previous_node = current_node
            current_node = current_node.get_next()

        temp_data = current_node.get_data()
        if current_index == 0 and current_node.get_next() is not None:
            self.head = current_node.get_next()
            return temp_data
        elif current_index == 0 and current_node.get_next() is None:
            self.head = None
            return temp_data
        else:
            previous_node.set_next(current_node.get_next())
            return temp_data
