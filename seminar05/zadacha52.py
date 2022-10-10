# Создайте программу для игры в конфеты. На столе 2021 одна конфета.
# Первый ход определяется жеребьевкой.
# За один ход можно забрать не больше 28 конфет.
# Кто делает последний ход тот и победитель.

from random import randint
import os
os.system("cls")

kol_konfet = 2021
max_konf_za_hod = 28

game = int(input('Выбери вариант: 1 - игра с человеком, 2 - игра с компьютером(игрок 1 -человек): '))
hod = randint(1, 2)
print(kol_konfet % (max_konf_za_hod + 1))
print(f'Первым ходит игрок номер: {hod}')
if game == 1:
    while kol_konfet >= 0:
        if hod == 1:
            igrok1 = int(input('Игрок 1, сколько конфет взять? = '))
            if igrok1 > max_konf_za_hod:
                print(f'Нельзя брать больше {max_konf_za_hod} конфет за один ход')
                continue
            elif igrok1 > kol_konfet:
                print(f'Столько конфет нет, осталось всего {kol_konfet}')
                continue
            if kol_konfet - igrok1 > 0:
                hod = 2
            kol_konfet -= igrok1
            print(f'Конфет осталось {kol_konfet}')
        else:
            igrok2 = int(input('Игрок 2, сколько конфет взять? = '))
            if igrok2 > max_konf_za_hod:
                print(f'Нельзя брать больше {max_konf_za_hod} конфет за один ход')
                continue
            elif igrok2 > kol_konfet:
                print(f'Столько конфет нет, осталось всего {kol_konfet}')
                continue
            if kol_konfet - igrok2 > 0:
                hod = 1
            kol_konfet -= igrok2
            print(f'Конфет осталось {kol_konfet}')
        if kol_konfet <= 0:
            break       
    print(f'Победил игрок {hod}! Проигравший отдаёт все конфету победителю!')
else:
    while kol_konfet >= 0:
        if hod == 1:
            igrok1 = int(input('Человек, сколько конфет взять? = '))
            if igrok1 > max_konf_za_hod:
                print(f'Нельзя брать больше {max_konf_za_hod} конфет за один ход')
                continue
            elif igrok1 > kol_konfet:
                print(f'Столько конфет нет, осталось всего {kol_konfet}')
                continue
            if kol_konfet - igrok1 > 0:
                hod = 2
            kol_konfet -= igrok1
        else:
            konf_pc = kol_konfet % (max_konf_za_hod + 1)
            if konf_pc == 0:
                konf_pc = randint(1,28)
            print(f'Компьютер берет {konf_pc}')
            if kol_konfet - konf_pc > 0:
                hod = 1
            kol_konfet -= konf_pc
            print(f'Конфет осталось {kol_konfet}')
        if kol_konfet <= 0:
            break
    if hod == 1:
        print('Победил человек! Проигравший отдаёт все конфету победителю!')
    else:
        print('Победил компьютер! Проигравший отдаёт все конфету победителю!')
