# Задайте список из N чисел, заполненный по формуле (1+1/N)**N и выведите на экран их сумму.
# для N = 6: [2,2,2,2,2,3] -> 13

number = int(input('Введите число N = '))
summa = 0
spisok = []
for i in range(1,number+1):
    spisok.append((1 + 1 / i)**i)
    summa += spisok[i-1]
    print(spisok)
print(summa)

