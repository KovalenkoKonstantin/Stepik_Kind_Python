# дополни код так, чтобы он выводил элементы списка l в обратном порядке
#
# Постарайся не использовать функцию reversed()
l = [54, 47, 49, 45, 51, 87, 82, 61, 98, 81, 76, 65, 99, 92, 19, 17, 27, 58, 66, 32, 11, 10, 30, 98,
     60, 67, 86, 82, 89, 95, 71, 59, 49, 11, 79, 55, 63, 23, 70, 38, 66, 81, 4, 49, 84, 10, 49, 23, 61,
     83, 32, 48, 42, 64, 90, 96, 66, 73, 7, 80, 62, 7, 13, 72, 15, 8, 68, 24, 94, 95, 37, 72, 2, 79, 13, 88,
     6, 5, 81, 83, 2, 90, 72, 12, 96, 73, 30, 2, 68, 52, 19, 35, 18, 34, 91, 88, 61, 67, 61, 30]
print(l[-1:-len(l) - 1:-1])
print(l[::-1])
