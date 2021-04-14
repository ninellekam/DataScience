import re
from functools import reduce
import operator


def solution1(args):
    return list(map(lambda x: int(reduce(lambda x, y: x + y, re.findall(r'\d', x))[::-1]), args))


def solution2(args):
    return list(map(lambda x: x[0] * x[1], list(args)))


def solution3(args):
    return list(filter(lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5, args))


def solution4(args):
    return list(filter(None, args))


def solution5(args):
    return list(map(lambda x: operator.setitem(x, 'square', x['length'] * x['width']), args))


def solution6(args):
    return list(map(lambda x: dict(x, square=x["length"] * x["width"]), args))


def solution7(args):
    return reduce(lambda x, y: x & y, args)


def solution8(args):
    return list(map(lambda my_dict:
                    reduce(lambda x, y: operator.setitem(my_dict, y, args.count(y)) or my_dict, args,
                           range(0, len(args) + 1)), [{}]))[0]


def solution9(args):
    return list(map(lambda student: student["name"], filter(lambda student: student["gpa"] > 4.5, args)))


def solution10(args):
    return list(filter(lambda x: sum(map(lambda y: int(y), x[0::2])) == sum(map(lambda y: int(y), x[1::2])), args))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
