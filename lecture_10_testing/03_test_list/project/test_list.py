import unittest

from project.extended_list import IntegerList


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_list = IntegerList(1, 2, 3, 4, 5, "John")

    def test_constructor(self):
        result = self.my_list.get_data()
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_add_element(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.add("John")
        self.assertEqual(str(context.exception), "Element is not Integer")
        self.assertEqual(self.my_list.add(6), [1, 2, 3, 4, 5, 6])

    def test_remove_element(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.remove_index(7)
        self.assertEqual(str(context.exception), "Index is out of range")
        self.assertEqual(self.my_list.remove_index(0), 1)

    def test_get_element(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.get(6)
        self.assertEqual(str(context.exception), "Index is out of range")
        self.assertEqual(self.my_list.get(1), 2)

    def test_insert_element(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.insert(7, 6)
        self.assertEqual(str(context.exception), "Index is out of range")

        with self.assertRaises(ValueError) as context:
            self.my_list.insert(0, 3.5)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.my_list.get_biggest(), 5)

    def test_get_index(self):
        self.assertEqual(self.my_list.get_index(5), 4)


if __name__ == "__main__":
    unittest.main()



