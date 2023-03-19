from abc import ABC, abstractmethod
from typing import List
from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")

        self.__capacity = value

    def get_bill(self):
        return self.price_for_reservation + sum(d.price for d in self.delicacy_orders)

    @abstractmethod
    def reserve(self, number_of_people: int):
        ...


