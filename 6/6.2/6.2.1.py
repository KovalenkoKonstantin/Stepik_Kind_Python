# Для удобной работы со строками используются срезы
#
# Синтаксис
#
# название_строки[начальный_индекс:конечный_индекс]
# возвращает строку,
# состоящую из символов с индексами от
# начального_индекса (включительно) до конечного индекса (не включительно)
s = "abcdefg"
a = s[1:5]
print(a)

s = "Какой-нибудь текст"
print(s[6:12])

# Можно не указывать начальный индекс,
# и тогда срез будет от начала строки до конечного индекса (не включительно)
#
# Если не указать конечный индекс,
# то срез будет от начала строки, до конца.
#
# Если не указывать ни начального,
# ни конечного индекса,
# то срез просто скопирует строку целиком.
s = "abcdefg"
print(s[1:])
print(s[:5])
print(s[:])

s = "1234567890"
print(s[2:])

s = "abcdefg"
print(s[-3:])

s = "Какой-нибудь текст"
print(s[-5:])

s = "текст"
print(s[1:-1])

s = "abracadabra"
print(s[:])
