from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("some name", "some type", "some sound")

    def test_correct_init(self):
        self.assertEqual(self.mammal.name, "some name")
        self.assertEqual(self.mammal.type, "some type")
        self.assertEqual(self.mammal.sound, "some sound")
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_make_sound_correct_output(self):
        self.assertEqual(self.mammal.make_sound(), "some name makes some sound")

    def test_info_returns_correct_string(self):
        self.assertEqual(self.mammal.info(), "some name is of type some type")


if __name__ == "__main__":
    main()
    