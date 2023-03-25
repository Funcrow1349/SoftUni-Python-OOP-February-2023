#   Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the result of a function with
#   the given tag and return the new result.

def tags(symbol):
    def decorator(func):
        def wrapper(*args):
            return f"<{symbol}>{func(*args)}</{symbol}>"

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
