# Сдача в магазине "Фикси"

# Представьте, что вы кассир в популярной сети продовольственных магазинов "Фикси". И вам нужно вернуть как можно более неудобным способом сдачу, собранную только монетами. При этом сдачу нужно вернуть минимальным количеством монет. В вашем распоряжении имеются монеты номиналом в 1, 5, 10 и 50 копеек и 1, 2, 5 и 10 руб.

# Формат входных данных

# На вход вашей программе подается неотрицательное число N - сумма сдачи в формате '%.2f'.

# Формат результата

# Выведите список монет, которые должен выдать кассир: номинал монеты и количество монет, разделенных символом табуляции.

# Порядок монет идет в соответствии с уменьшением их номинала. Номинал монеты печатается в рублях в формате '%5.2f'.

import collections
import operator


def min_coins(v, c):
    d = {}
    for i in v:
        d[i / 100] = 0
        while c != 0:
            if (c < i):
                break
            c -= i
            d[i / 100] += 1
    sorted_x = collections.OrderedDict(d)
    for key in sorted_x:
        if (sorted_x[key] != 0):
            print(format(key, '5.2f'), end='\t')
            print(sorted_x[key])


c = float(input())
c = c * 100
v = [0.01 * 100, 0.05 * 100, 0.10 * 100, 0.50 * 100, 1 * 100, 2 * 100, 5 * 100, 10 * 100]
v.sort(reverse=True)
min_coins(v, c)