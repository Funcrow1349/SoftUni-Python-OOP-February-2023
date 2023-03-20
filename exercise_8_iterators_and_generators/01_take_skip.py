#   Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement
#   the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given
#   step.

class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            current_num = self.num
            self.num += self.step
            self.count -= 1
            return current_num
        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

