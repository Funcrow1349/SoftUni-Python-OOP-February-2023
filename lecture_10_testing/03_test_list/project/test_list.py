import unittest

from extended_list import IntegerList


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_list = IntegerList(1, 2, 3, 4, 5, "John")

    def test_constructor(self):
        result = self.my_list.get_data()
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_add_element_if_correct_type(self):
        self.my_list.add(6)
        result = self.my_list.get_data()
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_add_element_if_incorrect_type(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.add("John")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_element_if_index_is_invalid_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.remove_index(7)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_remove_element_if_index_is_valid(self):
        self.assertEqual(self.my_list.remove_index(0), 1)

    def test_get_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.get(6)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_element_with_valid_index(self):
        self.assertEqual(self.my_list.get(1), 2)

    def test_insert_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.insert(7, 6)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_wrong_type_of_element_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.insert(0, 3.5)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_insert_correct_element_on_correct_index(self):
        self.my_list.insert(0, 0)
        result = self.my_list.get_data()
        self.assertEqual(result, [0, 1, 2, 3, 4, 5])

    def test_get_biggest_number_in_list(self):
        self.assertEqual(self.my_list.get_biggest(), 5)

    def test_get_index_of_element(self):
        self.assertEqual(self.my_list.get_index(5), 4)


if __name__ == "__main__":
    unittest.main()



