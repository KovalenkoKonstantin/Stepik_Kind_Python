# Напиши программу,
# которая считает строку,
# и выведет ее "центральный" символ
# (символ впереди которого и позади которого одинаковое количество символов),
# или строку "Нет центрального символа" (без кавычек),
# если в строке четное число символов.
s = input()
if len(s) % 2 == 0:
    print('Нет центрального символа')
else:
    print(s[int((len(s) - 1) / 2)])

s = input()
if len(s) % 2:
    print(s[len(s) // 2])
else:
    print("Нет центрального символа")
