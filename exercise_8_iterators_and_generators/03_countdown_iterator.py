#   Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator to
#   return each countdown number (from count to 0 inclusive), separated by a single space.

class countdown_iterator:
    def __init__(self, count: int):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.count <= 0:
            raise StopIteration

        self.count -= 1
        return self.count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")


