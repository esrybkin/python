# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

from random import randint


def isfloat(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


lengthList = input('Введите целое число')
while isfloat(lengthList) == False:
    lengthList = input('Введите целое число')
lengthList = int(lengthList)
myList = []
for elem in range(lengthList):
    myList.append(randint(0, lengthList))
print(myList)

myNewList = []
for elem in range(len(myList)):
    if myList.count(elem) == 1:
        myNewList.append(elem)
print(myNewList)