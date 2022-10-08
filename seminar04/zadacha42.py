# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


n = int(input('Введите число N = '))
spisok = []
for i in range(2, int(n**0.5)):
    if n % i == 0:
        count = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                count = 0
                break
        if count == 1:
            spisok.append(i)
print(spisok)
