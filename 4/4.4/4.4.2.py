# Напиши программу,
# которая считывает число и выводит "+" (без кавычек),
# если оно положительно, "-" (без кавычек),
# если оно отрицательно и строку "Число равно 0", если оно равно 0
# a = 1
a = int(input())
if a > 0:
    print('+')
elif a < 0:
    print('-')
else:
    print('Число равно 0')