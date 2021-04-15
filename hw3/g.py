from collections import defaultdict


def smartdict_nan(key):
    return lambda: 10 * key


N = 10
smartdict = {}
for key in range(N):
    val = defaultdict(smartdict_nan(key))
    smartdict[key] = val

# Lamda-функция принимая локальную переменную содержит ССЫЛКУ на нее, а не ЗНАЧЕНИЕ,
# поэтому передавая разные значения key
# мы затирали в памяти по месту key возвращаемые значения функции.
# Чтобы решить данную проблему, можно создать функцию,
# которая явно вызовет smartdict_nan(key) и вернет лямбда. или же другой вариант:
# можно создать в лямбда переменную
# и явно копирование key совершить
# defaultdict(lambda key_copy=key: smartdict_nan(key_copy))
