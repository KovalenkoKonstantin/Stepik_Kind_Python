# Когда на часах было h часов и m минут,
# Сакура поставила таймер на t минут.
# Нужно вывести сколько будет времени на часах,
# когда время на таймере истечет
# (на первой строчке количество часов,
# на второй строчке количество минут)
#
# В первой строчке вводится число h
#
# На второй строчке вводится число m
#
# На третьей строчке вводится число t
h = int(input())
m = int(input())
t = int(input())
# h = 8
# m = 0
# t = 90
print((h + (m + t) // 60) % 24)
print((m + t) % 60)