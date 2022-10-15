# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,*,/. Приоритет операций стандартный.
# 2+2 => 4
# 1+2*3 => 7
# Добавьте возможность применения скобок, меняющих приоритет операций.

def my_action(op, digit1, digit2):
    if op == '+':
        return digit1 + digit2
    elif op == '-':
        return digit1 - digit2
    elif op == '*':
        return digit1 * digit2
    elif op == '//':
        return digit1 // digit2


my_string = '1+2*3'
my_list_symbols = [i for i in my_string if not i.isdigit()]
my_list_digits = [i for i in my_string if i.isdigit()]
while '*' in my_list_symbols or '/' in my_list_symbols:
    for i, e in enumerate(my_list_symbols):
        if e in ('*', '/'):
            my_list_digits[i] = my_action(
                e, my_list_digits[i], my_list_digits[i+1])
            del my_list_digits[i+1]
            del my_list_symbols[i]
while len(my_list_symbols) > 0:
    for i, e in enumerate(my_list_symbols):
        my_list_digits[i] = my_action(
            e, my_list_digits[i], my_list_digits[i+1])
        del my_list_digits[i+1]
        del my_list_symbols[i]
print(my_list_digits)