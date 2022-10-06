# Задайте список из вещественных чисел. Напишите программу, которая найдет
# разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] -> 0.19


spisok = [1.1, 1.2, 3.1, 5, 10.01]
print(spisok)
leng = len(spisok)
maxZnach = round(spisok[4] % 1, 2)
minZnach = round(spisok[4] % 1, 2)
for elem in range(leng):
    if round(spisok[elem] % 1, 2) > maxZnach:
        maxZnach = round(spisok[elem] % 1, 2)
    elif round(spisok[elem] % 1, 2) < minZnach:
        minZnach = round(spisok[elem] % 1, 2)
print(maxZnach- minZnach)
