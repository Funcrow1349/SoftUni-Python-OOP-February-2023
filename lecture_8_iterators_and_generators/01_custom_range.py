#   Create a class called custom_range that receives a start (int) and an end (int) upon initialization. Implement
#   the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).

class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            current_num = self.start
            self.start += 1
            return current_num
        else:
            raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)


