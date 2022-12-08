# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

subs = [1, 3, 5, 4, 9, 5, 14, 5, 1]
print(subs)
alone = []
for i in range (0, len(subs)):
    duplicate = 0
    for j in range(0, len(subs)):
        if i != j:
            if subs[i] == subs[j]:
                duplicate = 1
    if duplicate == 0:
        alone.append(subs[i])
print(alone)

