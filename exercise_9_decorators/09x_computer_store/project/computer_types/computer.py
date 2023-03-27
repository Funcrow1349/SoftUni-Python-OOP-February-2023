from abc import ABC, abstractmethod
from math import log2, ceil, floor


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    @abstractmethod
    def type(self):
        ...

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)
        return ceil(result) == floor(result)

    def set_parts(self, processor, ram):
        self.processor = processor
        self.ram = ram
        self.price += int(log2(ram)) * 100
        self.price += self.available_processors[processor]

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if not self.power_of_two(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"