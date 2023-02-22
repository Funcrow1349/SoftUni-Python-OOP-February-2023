# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:

def create_rhombus(size):
    for x in range(1, size + 1):
        space_data = size - x
        stars_date = x
        print(f"{space_data * ' '}{stars_date * '* '}")
    for x in range(size - 1, - 1, - 1):
        space_data = size - x
        stars_date = x
        print(f"{space_data * ' '}{stars_date * '* '}")


create_rhombus(int(input()))