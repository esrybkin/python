def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input())
    return choice

def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

# def read_csv(filename: str) -> list:
#     data = []
#     fields = ["Фамилия", "Имя", "Телефон", "Описание"]
#     with open(filename, 'r', encoding='utf-8') as fin:
#         for line in fin:
#             record = dict(zip(fields, line.strip().split(',')))
#             data.append(record)