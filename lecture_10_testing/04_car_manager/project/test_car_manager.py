from unittest import TestCase, main
from car_manager import Car


class CarManagerTests(TestCase):
    def setUp(self):
        self.my_car = Car("some make", "some model", 6, 55)

    def test_correct_init(self):
        self.assertEqual(self.my_car.make, "some make")
        self.assertEqual(self.my_car.model, "some model")
        self.assertEqual(self.my_car.fuel_consumption, 6)
        self.assertEqual(self.my_car.fuel_capacity, 55)
        self.assertEqual(self.my_car.fuel_amount, 0)

    def test_make_is_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.make = ""
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_is_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.model = ""
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_amount = -2
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_valid(self):
        self.my_car.refuel(50)
        self.assertEqual(self.my_car.fuel_amount, 50)

    def test_refuel_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_valid(self):
        self.my_car.refuel(7)
        self.my_car.drive(100)
        self.assertEqual(self.my_car.fuel_amount, 1)

    def test_drive_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.drive(100)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")


if __name__ == "__main__":
    main()
