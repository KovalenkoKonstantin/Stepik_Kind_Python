# Напиши программу, которая считает строку s и выведет:
#
# Все символы строки с индексами от 3 (включительно) до 9 (не включительно)
# Все символы строки с индексами от 3 (включительно) до 9 (включительно)
# Первые 5 символов строки
# Последние 5 символов строки
# Каждый пункт нужно выводить с новой строки
s = input()
print(s[3:9:1])
print(s[3:10:1])
print(s[:5:1])
print(s[-5::1])

print((s := input())[3:9], s[3:10], s[:5], s[-5:], sep='\n')