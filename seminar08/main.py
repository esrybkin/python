from modules import *
BASE = 'database.csv'

choice = show_menu()
while choice != 9:
    if choice == 1:
        print('Найти сотрудника')
    elif choice == 2:
        print('Выбор сотрудника по должности')
    elif choice == 3:
        print('Выбор сотрудника по зарплате')
    elif choice == 4:
        employees = get_info()
        creating(employees)
    elif choice == 5:
        print('Удалить сотрудника')
    elif choice == 6:
        print('Обновить сотрудника')
    elif choice == 7:
        write_json()
    elif choice == 8:
        write_csv()
    elif choice == 9:
        exit()

