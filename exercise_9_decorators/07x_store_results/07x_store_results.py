#   Create a class called store_results. It should be used as a decorator and store information about the executed
#   functions in a file called results.txt in the format: "Function {func_name} was called. Result: {func_result}"

class store_results:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open("results.txt", "a") as result_file:
            result_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
