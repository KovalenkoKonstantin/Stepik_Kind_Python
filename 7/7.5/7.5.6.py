# Дополни код так, чтобы в список l были добавлены все элементы списка l2, а потом все элементы списка l3
l = [1, 2, 3, 4]
l2 = [39, 1024, 2023]
l3 = [666, 86, 277353]

# l.extend(l2)
# l.extend(l3)
l += l2 + l3

print(l)
