# Напиши программу,
# которая считает координаты двух клеток шахматной доски,
# и выведет "YES" (без кавычек) если они одного цвета,
# и "NO" (без кавычек) в противном случае.
# На первых двух строчках вводятся координаты первой клетки,
# на третьей и четвертой строчке вводятся координаты второй клетки.
# Все координаты - целые числа от 1 до 8 включительно
# Подумай, что общего между суммой координат по x и y у клеток одного цвета
a = int(input())
b = int(input())
c = int(input())
d = int(input())
# a = 1
# b = 1
# c = 2
# d = 2
if (a + b) % 2 == (c + d) % 2:
    print("YES")
else:
    print("NO")
