# Напиши программу,
# которая считает 2 числа - n и k
# и выводит количество способов выбрать k элементов
# из множества из n объектов
# (объекты считать различными, порядок выбора не важен)
#
# Число способов выбрать k элементов
# из множества из n элементов
# называется C из n по k, и вычисляется по формуле
# n! / (k! (n - k)!)
# (С помощью восклицательного знака записывается факториал,
# например n! - это факториал числа n)
import math

n = int(input())
k = int(input())

# print(math.comb(n, k))

# math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

nn = 1
kk = 1
for t in range(1, min(k, n - k) + 1):
    nn *= n
    kk *= t
    n -= 1
print(nn // kk)
