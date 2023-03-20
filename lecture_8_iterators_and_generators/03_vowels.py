#   Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods, so the
#   iterator returns only the vowels from the string.

class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            current_letter = self.string[self.index]
            self.index += 1
            if current_letter in self.vowels:
                return current_letter
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
