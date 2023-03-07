from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salaries = sum(w.salary for w in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_care = sum(a.money_for_care for a in self.animals)
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        animal_info = {"Lion": [], "Tiger": [], "Cheetah": []}
        [animal_info[a.__class__.__name__].append(str(a)) for a in self.animals]

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(animal_info['Lion'])} Lions:",
            *animal_info["Lion"],
            f"----- {len(animal_info['Tiger'])} Tigers:",
            *animal_info["Tiger"],
            f"----- {len(animal_info['Cheetah'])} Cheetahs:",
            *animal_info["Cheetah"],
        ]

        return "\n".join(result)

    def workers_status(self):
        worker_info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [worker_info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(worker_info['Keeper'])} Keepers:",
            *worker_info["Keeper"],
            f"----- {len(worker_info['Caretaker'])} Caretakers:",
            *worker_info["Caretaker"],
            f"----- {len(worker_info['Vet'])} Vets:",
            *worker_info["Vet"],
        ]

        return "\n".join(result)


