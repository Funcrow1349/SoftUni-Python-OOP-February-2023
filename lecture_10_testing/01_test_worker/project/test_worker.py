class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 2500, 10)

    def test_correct_init(self):
        self.assertEqual(self.worker.name, "Ivan")
        self.assertEqual(self.worker.salary, 2500)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_energy_incremented_correctly(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_if_raising_error_when_energy_is_zero_or_negative(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_salary_increased_properly(self):
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary)

    def test_energy_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_get_info_method(self):
        result = self.worker.get_info()
        self.assertEqual(result, f'{self.worker.name} has saved {self.worker.money} money.')


if __name__ == "__main__":
    unittest.main()

