def vowel_filter(function):
    def wrapper():
        return [l for l in function() if l.lower() in "aeiouy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
