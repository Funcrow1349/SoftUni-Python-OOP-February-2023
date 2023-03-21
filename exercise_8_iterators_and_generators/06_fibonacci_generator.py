#   Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two
#   numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current
#   number with the previous one.

def fibonacci():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


generator = fibonacci()
for i in range(5):
    print(next(generator))
