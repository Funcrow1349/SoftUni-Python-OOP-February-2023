import unittest
from cat import Cat


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Tom")

    def test_cat_size_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), 'Already fed.')

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()

