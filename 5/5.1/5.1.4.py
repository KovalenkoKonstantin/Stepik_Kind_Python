# Напиши программу,
# которая поздоровается с n людьми
# и выведет строку "Привет, <введенное_имя>" (без кавычек)
# На первой строке вводится целое число n
# На следующих n строках вводится по имени.
n = int(input())
for i in range(n):
    x = str(input())
    for j in range(n):
        print('Привет, ' + x)


for i in range(int(input())):
    print('Привет, ' + input())

# input -- это всегда строка, приводить строку к виду строки бессмысленно
