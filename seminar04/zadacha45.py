# Даны два файла. В каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('z45file.txt','r') as file:
    poly_1 = file.readline()
    list_poly_1 = poly_1.split()
with open('z45file2.txt','r') as file:
    poly_2 = file.readline()
    list_poly_2 = poly_2.split()
sum_poly = list_poly_1 + list_poly_2
with open('z45file3.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_poly_1} + {list_poly_2}')
