from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    def validate_order(self, booth_number, item_name, collection):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            item = next(filter(lambda x: x.name == item_name, collection))
        except StopIteration:
            raise Exception(f"No {item_name} in the pastry shop!")

        return booth, item

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for d in self.delicacies:
            if d.name == name:
                raise Exception(f"{d.name} already exists!")

        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            delicacy = Stolen(name, price)
        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for b in self.booths:
            if b.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            booth = PrivateBooth(booth_number, capacity)
        else:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                b.reserve(number_of_people)
                return f"Booth {b.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth, delicacy = self.validate_order(booth_number, delicacy_name, self.delicacies)
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        bill = booth.get_bill()
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        self.income += bill

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."



