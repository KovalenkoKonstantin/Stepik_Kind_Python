# Дано число в десятичной системе счисления.
# Нужно вывести его предпоследнюю цифру,
# если бы оно было записано в двоичной системе счисления.
print(bin(int(input()))[-2])
# Пользователь вводит число,
# которое преобразуется в двоичное
# - затем с помощью среза (тех "[]") мы обращаемся к предпоследнему элементу.