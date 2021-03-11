# Анаграммы 2.0: Предложения

# На вход программе подаются два предложения, каждое предложение начинается с новой строки. Необходимо проверить, можно ли получить второе предложения из первого с помощью перестановки и удаления слов. Если такое возможно, напечатайте YES, в противном случае - NO.

import sys
from collections import Counter
n = input().split(' ')
b = input().split(' ')
n = [el.lower() for el in n]
b = [el.lower() for el in b]
n = Counter(n)
b = Counter(b)
for key in b:
    if key not in n or b[key] > n[key]:
        print("NO")
        sys.exit()
print("YES")