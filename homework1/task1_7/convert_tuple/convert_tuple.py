from functools import reduce


def convert_tuple_to_integer(t):
    return int(reduce(lambda n1, n2: f"{n1}{n2}", t))


print(convert_tuple_to_integer((1, 2, 3, 4)))
