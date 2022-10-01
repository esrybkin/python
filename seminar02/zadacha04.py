# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N,N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Nuimber of elements: 5
# -> [-5, -4, -3, -2, -1, 0 ,1 ,2 ,3 , 4, 5]
# -> 15

number = int(input('Введите число элементов N = '))
pos1 = int(input('Введите номер первой позиции = '))
pos2 = int(input('Введите номер второй позиции = '))
spisok = []
for i in range(-number, number + 1):
    spisok.append(i)
print(spisok)
print(spisok[pos1-1]*spisok[pos2-1])