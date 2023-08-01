# Списковый метод pop() принимает одно число - индекс элемента,
# и удаляет элемент с этим индексом, возвращая его значение.
# Если элемента с таким индексом нет, то произойдет ошибка.
# Индекс может быть отрицательным.
l = [1, 2, 3, 4, 5, 1, 2]
temp = l.pop(2) # удаляет элемент с индексом 2 (т. е. число 3)
print(temp) # выведем значение удаленного элемента
print(l)
# Если у pop() не будет указан индекс, то он удалит последний элемент списка
l = [1, 2, 3, 4, 5, 1, 2]
print(l.pop()) # удаляет последний элемент списка (т. е. число 2)
print(l)