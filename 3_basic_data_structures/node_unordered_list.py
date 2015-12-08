class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


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
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            current = self.head
        current_index = 0
## Currently broken because index is not a declared variable
        while current_index != index:
            current_index += 1
            current = current.get_next()
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

# Index method has time complexity O(n) since it traverses the list until it reaches the correct index.
    def index(self, index):
        current = self.head
        current_index = 0
        while current_index != index:
            current_index += 1
            current = current.get_next()
        return current.get_data()

# Append method has time complexity O(n) since it traverses the entire list to find the last node.
    def append(self, item):
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        new_node = Node(item)
        current.set_next(new_node)

# Insert method has time complexity O(n) since it traverses the list until is reaches the correct index.
# Inserts into index after the current index. Must fix!
    def insert(self, index, item):
        current = self.head
        current_index = 0
        while current_index != index:
            current_index += 1
            current = current.get_next()

        temp_node = current.get_next()
        new_node = Node(item)
        current.set_next(new_node)
        new_node.set_next(temp_node)

# Pop method is O(n) since it must traverse the list to find the correct index.
# Added default index parameter to mimic behavior of regular Python list.pop() method.
# unordered_list.pop() using default index is O(n) since 2n time complexity is still n.
    def pop(self, index=None):
        if index is None:
            index = self.size() - 1

        current = self.head
        previous = None
        current_index = 0

        while current_index != index:
            current_index += 1
            previous = current
            current = current.get_next()

        temp_data = current.get_data()
        if current_index == 0 and current.get_next() is not None:
            self.head = current.get_next()
            return temp_data
        elif current_index == 0 and current.get_next() is None:
            self.head = None
            return temp_data
        else:
            previous.set_next(current.get_next())
            return temp_data