# У строк и списков много общего,
# например срезы, которыми мы уже пользовались в предыдущем модуле, можно использовать и на списках
# Синтаксис:
#
# название_списка[начальный_индекс:конечный_индекс:шаг]
# возвращает новый список,
# в который входят элементы списка "название_списка"
# с индексами от начального_индекса (включительно)
# до конечного_индекса (не включительно)
l = [1, 5, 27, 39, 12345, 381, 347]
print(l[2::2])
# Можно не писать шаг (и второе двоеточие), и тогда шаг будет равен 1
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[3:9])
# Как и в случае со строками, индексы и шаг могут быть отрицательными.
