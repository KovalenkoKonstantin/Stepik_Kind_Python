# Напиши программу,
# которая считывает натуральное число n
# и n чисел,
# каждое на своей строчке,
# и выводит только те числа,
# которые делятся на свой порядковый номер (нумерация начинается с 1).
for i in range(int(input())):
    j = int(input())
    if j % (i + 1) == 0:
        print(j)
