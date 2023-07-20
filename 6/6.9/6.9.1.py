# Для того, чтобы убрать все пробельные символы в начале строки можно использовать строковый метод lstrip()
#
# Чтобы убрать пробельные символы в конце строки используется строковый метод rstrip
#
# Чтобы убрать все пробельные символы и в начале и в конце строки, можно использовать строковый метод strip()

s = "   Hello world    "
print("'", s.lstrip(), "'", sep='')
print("'", s.rstrip(), "'", sep='')
print("'", s.strip(), "'", sep='')