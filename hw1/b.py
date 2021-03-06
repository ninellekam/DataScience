# Сложная сортировка

# Дан массив a1,...,an из n натуральных чисел.

# Требуется отсортировать числа в массиве в порядке возрастания суммы цифр, а при равной сумме цифр — по возрастанию самого числа.

# Формат входных данных

# В первой строке задается число n (3 ≤ n ≤ 1000).

# Во второй — задаются n натуральных чисел a1,...,an через пробел (0 ≤ ak ≤ 1000).

# Формат результата

# Выведите отсортированный список чисел через пробел.
# Решение:

def summ(i):
    number = i
    sum = 0
    while i != 0:
        sum += i % 10
        i //= 10
    return (sum, number)
n = int(input())
b = input()
a = b.split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
a.sort(key=summ)
print(*a)