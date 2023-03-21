#   Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an
#   iterator to return the given elements, so they form a string with a length - the given number. If the number is
#   greater than the number of elements, then the sequence repeats as necessary.

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.number - 1:
            raise StopIteration

        self.iterations += 1
        index = self.iterations % len(self.sequence)
        return self.sequence[index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
