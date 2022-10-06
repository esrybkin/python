# Напишите программу, которая найдёт произведение пар чисел из списка. Парой считаем
# первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] -> [12, 15, 16]
# [2, 3, 5, 6] -> [12, 15]
import math
spisok = [2, 3, 4, 5, 6, 7, 8]
print(spisok)
proizv = 0
leng = len(spisok)
for i in range(leng//2):
    proizv = spisok[i] * spisok[len(spisok) - i - 1]
    print(proizv, end=' ')
if leng % 2 != 0 :
    print(spisok[math.floor(leng/2)]**2)