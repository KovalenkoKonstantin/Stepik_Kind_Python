# Отметь номера всех кусков кода, которые выведут все элементы списка l
l = [1, 2, 3, 4, 5]
print(l[-len(l) + 1:]) # No

l = [1, 2, 3, 4, 5]
print(l[:][:]) # Yes
# копия копии списка

l = [1, 2, 3, 4, 5]
print(l[1:5]) # No

l = [1, 2, 3, 4, 5]
print(l[-len(l)::]) # Yes

l = [1, 2, 3, 4, 5]
print([l[0]] + l[1:]) # Yes
print([l[0]])
print([l[1:]])