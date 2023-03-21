#   Create a generator function called get_primes() which should receive a list of integer numbers and return a list
#   containing only the prime numbers from the initial list.

def get_primes(list_of_integers):
    for x in list_of_integers:
        if x <= 1:
            continue

        for d in range(2, x):
            if x % d == 0:
                break
        else:
            yield x


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
