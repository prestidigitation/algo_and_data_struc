from ordered_list import OrderedList
import unittest


class TestOrderedList(unittest.TestCase):

    def set_up(self):
        self.my_list = OrderedList()
        self.my_list.add(31)
        self.my_list.add(77)
        self.my_list.add(17)
        self.my_list.add(93)
        self.my_list.add(26)
        self.my_list.add(54)

        self.values = [(1, 31),
                       (2, 77),
                       (3, 17),
                       (4, 93),
                       (5, 26),
                       (6, 54)]

    def test_is_empty(self):
        new_list = OrderedList()
        self.assertTrue(new_list.is_empty())

    def test_add(self):
        pass

    def test_size(self):
        new_list = OrderedList()
        size_counter = 0
        self.assertEqual(0, new_list.size())
        for num, value in self.values:
            new_list.add(value)
            size_counter += 1
            self.assertEqual(size_counter, new_list.size())

    def test_search(self):
        for num, value in self.values:
            self.assertTrue(self.values(value))

if __name__ == '__main__':
    unittest.main()
