# Напиши программу,
# которая считает координаты двух шахматных ладей,
# и выведет "YES" (без кавычек) если они бьют друг друга,
# и "NO" (без кавычек) в противном случае.
# Ладья бьет другую фигуру,
# если находится с ней на одной вертикали или на одной горизонтали.
# На первых двух строчках вводятся координаты первой ладьи,
# на третьей и четвертой строчке вводятся координаты второй ладьи.
# Все координаты - целые числа от 1 до 8 включительно

# нумерация начинается из левого верхнего угла
# вначале вводится вертикальная составляющая координаты,
# потом горизонтальная
a = int(input())
b = int(input())
c = int(input())
d = int(input())
# a = 1
# b = 1
# c = 2
# d = 2
if a == c or b == d:
    print("YES")
else:
    print("NO")

x, y = int(input()), int(input())
if x == int(input()) or y == int(input()):
    print("YES")
else:
    print("NO")
    