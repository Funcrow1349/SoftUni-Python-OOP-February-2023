#   Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the
#   iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).

class dictionary_iter:
    def __init__(self, dictionary):
        self.items = list(dictionary.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.items) - 1:
            raise StopIteration

        self.idx += 1
        return self.items[self.idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

