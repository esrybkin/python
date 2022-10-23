from copyreg import pickle
import csv
import json
from pathlib import Path
BASE = 'database.csv'

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def get_info():
    info = {}
    info["id"] = " "
    info["last name"] = input('Введите фамилию: ')
    info["name"] = input('Введите имя: ')
    info["position"] = input('Введите должность: ')
    info["phone number"] = input('Введите телефон: ')
    info["salary"] = input('Введите оклад: ')
    return info


def creating(data):
    with open (BASE, 'a', encoding = 'utf-8') as file:
        for key, value in data.items():
            file.writelines(f'{key};{value};')
    print('Запись сохранена...')


def read_csv() -> list:
    employee = []
    with open(BASE, 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


def read_json() -> list:
    employee = []
    with open(BASE, 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee


def write_csv(employees: list):
    with open(BASE, 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.value())


def write_json(employees: list):
    with open(BASE, 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')


# def find_position(employees: list):
#     data = {}
#     with open(BASE, 'r', encoding='utf-8') as fout:
#         for line in fout:
#             if data["position"] == 
#             record = dict(zip(fields, line.strip().split(',')))
#             data.append(record)
#     return data
