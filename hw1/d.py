# Сумма конкатенаций

# На стандартный поток ввода подаются два числа N и K. Напишите программу, которая по заданным числам вычисляет число: N + NN + NNN + ... + N...N, где N...N - число, составленное конкатенацией K раз числа N.

# Формат входных данных

# На вход вашей программе подаются два целых неотрицательных числа N и K, где N - число, которое нужно повторить K раз. Числа разделены пробелом.

# Формат результата

# Выведите получившееся число.

t = input()
n = int(t.split(' ')[0])
k = int(t.split(' ')[1])
n = str(n)
sum = 0
for i in range(1, k + 1):
    s = n*i
    m = int(s)
    sum += m
print(sum)