# В государстве X запрещено n слов,
# за каждое использование каждого из которых (вне зависимости от регистра)
# полагается штраф в k единиц местной валюты
#
# Напишите программу,
# которая посчитает штраф за использования строки s,
# в которой есть запрещенные слова.
#
# В первой строчке вводится число n
#
# Во второй строчке вводится число k
#
# На третьей строчке вводится строка s.
#
# На следующих n строчках
# вводится по одному запрещенному слову в нижнем регистре
n = input()  # количество слов
k = input()  # величина штрафа
s = input()  # строка
n = 3
k = 100
s = 'Придумайте какую-нибудь кРаКаЗяБрУ для кУрСА по алгебре. Не забудьте использовать интерполяционый многочлен в решении'
x = input()
for x in n - 1:
   print(s.count(x))
   