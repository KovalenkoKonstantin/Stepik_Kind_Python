# Напиши программу,
# которая считает строку s
# и выведет ее первые 5 символов,
# после чего будет выводить многоточие ("...")
# Если в строке s не более 5 символов,
# то выводить многоточие не нужно
s = input()
if len(s) > 5:
    print(s[0:5]+'...')
else:
    print(s[0:5])

s = input()
print(s[:5] + '...' * (len(s) > 5))
