# Тоши хочет написать программу,
# которая уберет все оценки равные 4 или 5
# из электронного дневника Сакуры,
# но так как он забыл python,
# потому что все время программировал на C++,
# он не может решить эту сложную задачу.
# Помогите Тоши и напишите программу,
# которая считает оценки Сакуры,
# и выведет только те, которые нужно оставить
# На первой строке вводится количество оценок сакуры - n
# На следующих n строках вводится
# по одной оценке - целому числу от 1 до 5
# Программа должна выводить оставшиеся оценки сакуры,
# каждую на отдельной строчке.
n = int(input())
for i in range(n):
    x = int(input())
    if 0 < x < 4:
        print(x)

for x in range(int(input())):
    a = int(input())
    0 < a < 4 and print(a)
