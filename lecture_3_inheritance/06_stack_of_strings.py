#   Create a class Stack that can store only strings and has the following functionality:
#   •	Instance attribute: data: list
#   •	Method: push(element) – adds an element at the end of the stack
#   •	Method: pop() – removes and returns the last element in the stack
#   •	Method: top() - returns a reference to the topmost element of the stack
#   •	Method: is_empty() - returns boolean True/False
#   •	Override the string method to return the stack data in the format:
#       "[{element(N)}, {element(N-1)} ... {element(0)}]"

from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "[" + ", ".join([f"{self.data[i]}" for i in range(len(self.data) - 1, - 1, - 1)]) + "]"


some_stack = Stack()
some_stack.push("Ivan")
some_stack.push("Dragan")
some_stack.push("Stoyan")
some_stack.push("Boyan")
print(some_stack.pop())
print(some_stack.top())
print(some_stack.is_empty())
print(some_stack.__str__())