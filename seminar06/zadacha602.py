# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечетных позициях 3 и 9. Ответ: 12

spisok = [2, 3, 5, 9, 3]
my_list = [elem for i, elem in enumerate(spisok) if i % 2 != 0]
print(sum(my_list))