# Оставить различные

# Дан массив a из n целых чисел. Напишите программу, которая выведет:
# 1. исходный список чисел без дубликатов с сохранением порядка;
# 2. количество чисел, которые были удалены из массива.

# Формат входных данных

# В первой строке число n (1 ≤ n ≤ 100000). Во второй строке записаны n целых чисел ai (1 ≤ ai ≤ 10000).

# Формат результата

# Выведите в первой строке список уникальных чисел. Во второй строке число удаленных элементов.
# Решение:

n = int(input())
b = input()
a = b.split(' ')
niko = 0
list_tmp = []
for i in a:
    if i not in list_tmp:
        list_tmp.append(i)
    else:
        niko += 1
print(*list_tmp)
print(niko)