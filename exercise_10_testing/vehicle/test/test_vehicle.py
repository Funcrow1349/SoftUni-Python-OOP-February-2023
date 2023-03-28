from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(60, 101)

    def test_init_correct_data(self):
        self.assertEqual(self.vehicle.fuel, 60)
        self.assertEqual(self.vehicle.capacity, 60)
        self.assertEqual(self.vehicle.horse_power, 101)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(30)
        self.assertEqual(self.vehicle.fuel, 22.5)

    def test_refuel_if_capacity_is_exceeded(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(2)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_if_capacity_not_exceeded(self):
        self.vehicle.fuel = 30
        self.vehicle.refuel(20)
        self.assertEqual(self.vehicle.fuel, 50)

    def test__str__returns_correct_string(self):
        self.assertEqual(
            "The vehicle has 101 " +
            "horse power with 60 fuel left and 1.25 fuel consumption",
            str(self.vehicle)
        )


if __name__ == "__main__":
    main()
