from ordered_list import OrderedList
import unittest


class TestOrderedList(unittest.TestCase):

    def set_up(self):
        self.my_list = OrderedList()
        self.my_list.add(31)
        self.my_list.add(77)
        self.my_list.add(17)
        self.my_lits.add(93)
        self.my_list.add(26)
        self.my_list.add(54)

    def test_is_empty(self):
        new_list = OrderedList()
        self.assertTrue(new_list.is_empty())

    # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
