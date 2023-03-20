#   Create a generator function called genrange that receives a start (int) and an end (int) upon initialization. It
#   should generate all the numbers from the start to the end (inclusive).

def genrange(start, end):
    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))