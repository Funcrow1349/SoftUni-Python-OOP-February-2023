#   Create a generator function called squares that should receive a number n. It should generate the squares of all
#   numbers from 1 to n (inclusive).

def squares(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1


print(list(squares(5)))