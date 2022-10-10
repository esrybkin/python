# Написать программу алгоритма RLE

import os
os.system("cls")

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

original_string = rle_encode('BBBBBBBBBBRRRRRRRRRRAAABAAAFDDCCNNNNNNNNNNNNCCCCCAEEEEEEEEEEEEEEEEE')
encrypt_string = original_string
print('Зашифрованные данные:')
print(original_string)

decoded_val = rle_decode(encrypt_string)
print('Расшифрованные данные:')
print(decoded_val)