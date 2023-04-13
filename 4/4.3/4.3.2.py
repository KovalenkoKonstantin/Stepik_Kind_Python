# Напиши программу,
# которая считает три положительных целых числа a, b и c,
# каждое на своей строке
# и выведет "YES" (без кавычек),
# если существует треугольник со сторонами a b и с, и "NO" (без кавычек)
#
# Вырожденный треугольник считается треугольником.
# Треугольник с заданными длинами сторон существует,
# если сумма длин любых двух сторон больше
# (или равна в случае вырожденного треугольника)
# длине оставшейся стороны

# a = 2
# b = 2
# c = 3
a = int(input())
b = int(input())
c = int(input())
if a + b >= c and a + c >= b and b + c >= a:
    print('YES')
else:
    print('NO')