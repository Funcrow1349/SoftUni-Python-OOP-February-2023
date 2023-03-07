#   Create a class called Mammal. Upon initialization, it should receive a name, a type, and a sound. Create a class
#   attribute called kingdom which should not be accessed outside the class and set it to be "animals". Create three
#   more instance methods:
#   •	make_sound() - returns a string in the format "{name} makes {sound}"
#   •	get_kingdom() - returns the private kingdom attribute
#   •	info() - returns a string in the format "{name} is of type {type}"

class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, animal_type: str, sound: str):
        self.name = name
        self.type = animal_type
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
