#   Create a generator function called reverse_text that receives a string and yields all string characters on one line
#   in reversed order.

def reverse_text(string):
    for char in reversed(string):
        yield char


for char in reverse_text("step"):
    print(char, end='')
