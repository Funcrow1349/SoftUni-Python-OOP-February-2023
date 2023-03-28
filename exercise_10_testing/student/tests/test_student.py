from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("Ivan", None)

    def test_init_correct_data_when_courses_is_not_none(self):
        self.student.courses = {"OOP": ["some note"]}
        self.assertEqual(self.student.name, "Ivan")
        self.assertEqual(self.student.courses, {"OOP": ["some note"]})

    def test_init_correct_data_when_courses_is_none(self):
        self.assertEqual(self.student.name, "Ivan")
        self.assertEqual(self.student.courses, {})

    def test_enroll_when_course_name_is_in_the_dictionary(self):
        self.student.courses = {"OOP": ["some note"]}
        result = self.student.enroll("OOP", [1, 2, 3])
        self.assertEqual(self.student.courses, {"OOP": ["some note", 1, 2, 3]})
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_when_course_name_not_in_dict_and_course_notes_y_or_empty_space(self):
        result = self.student.enroll("OOP", [1, 2, 3])
        self.assertEqual(self.student.courses, {"OOP": [1, 2, 3]})
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_when_course_name_not_in_dict_and_course_notes_are_not_default(self):
        result = self.student.enroll("OOP", [1, 2, 3], "some new notes")
        self.assertEqual(self.student.courses, {"OOP": []})
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_when_course_exists(self):
        self.student.courses = {"OOP": ["some note"]}
        result = self.student.add_notes("OOP", [1, 1])
        self.assertEqual(self.student.courses, {"OOP": ["some note", [1, 1]]})
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("OOP", [1, 1])
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_course_if_course_exists(self):
        self.student.courses = {"OOP": ["some note"]}
        result = self.student.leave_course("OOP")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(result, "Course has been removed")

    def test_leave_course_if_course_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("OOP")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()
