# Дополни код так, чтобы в список l было добавлено число 39
#
# Список l выводить не нужно
l = [1, 2, 3, 4]
l = [1, 2, 3, 4, 39]
l.append(39)
l += [39]
l = [1, 2, 3, 4] + [39]
l.insert(len(l)+1, 39)