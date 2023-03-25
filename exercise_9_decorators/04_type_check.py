#   Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the
#   parameter passed to the decorated function is of the type given to the decorator. If it is, execute the function
#   and return the result, otherwise return "Bad Type".


def type_check(type_of_parameter):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if isinstance(arg, type_of_parameter):
                    return func(arg)

                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
