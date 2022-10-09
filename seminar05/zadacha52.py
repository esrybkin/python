# Создайте программу для игры в конфеты. На столе 2021 одна конфета.
# Первый ход определяется жеребьевкой.
# За один ход можно забрать не больше 28 конфет.
# Кто делает последний ход тот и победитель.

from random import randint
import os
os.system("cls")

kol_konfet = 99
max_konf_za_hod = 28

hod = randint(1, 2)
print(f'Первым ходит игрок номер: {hod}')
print(kol_konfet % (max_konf_za_hod + 1))

while kol_konfet >= 0:
    if hod == 1:
        igrok1 = int(input('Игрок 1, сколько конфет взять? = '))
        if igrok1 > max_konf_za_hod:
            print(f'Нельзя брать больше {max_konf_za_hod} конфет за один ход')
            continue
        elif igrok1 > kol_konfet:
            print(f'Столько конфет нет, осталось всего {kol_konfet}')
            continue
        kol_konfet -= igrok1
        print(f'Конфет осталось {kol_konfet}')
        hod = 2
    if hod == 2:
        igrok2 = int(input('Игрок 2, сколько конфет взять? = '))
        if igrok2 > max_konf_za_hod:
            print(f'Нельзя брать больше {max_konf_za_hod} конфет за один ход')
            continue
        elif igrok2 > kol_konfet:
            print(f'Столько конфет нет, осталось всего {kol_konfet}')
            continue
        kol_konfet -= igrok2
        hod = 1
        # print(kol_konfet % (max_konf_za_hod + 1))
        print(f'Конфет осталось {kol_konfet}')
print(f'Победил игрок {hod}! Проигравший отдаёт все конфету победителю!')