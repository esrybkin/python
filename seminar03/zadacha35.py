# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k=8 список будет выглядеть:
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8 ,13 , 21]
# Негафибоначчи.


n = int(input('Введите число = '))
fib = [0]
count = 1
if n > 0:
    fib = [1, 0, 1]
while count<n:
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    if count % 2:
        fib.insert(0, fib[len(fib) - 1])
    else:
        fib.insert(0, -fib[len(fib) - 1])
    count += 1
print(fib)