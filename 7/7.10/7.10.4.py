# Отметь номера всех кусков кода, которые выведут все элементы списка l
l = [1, 2, 3, 4, 5]
print(l) # Yes

l = [1, 2, 3, 4, 5]
print(l[::]) # Yes

l = [1, 2, 3, 4, 5]
print(l[:]) # Yes

l = [1, 2, 3, 4, 5]
print(l[len(l):0]) # No

l = [1, 2, 3, 4, 5]
print(l[0:len(l)]) # Yes
