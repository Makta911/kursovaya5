from kurs5.db.managers import PostgresDBManager
from prettytable import PrettyTable

def print_employers():
    db_manager = PostgresDBManager()
    try:
        res = db_manager.get_companies_and_vacancies_count()
    finally:
        db_manager.disconnect()

    table = PrettyTable(field_names=['Название компании', 'Количество вакансий'])
    for data in res:
     table.add_row([data[0], data[1]])

    print(table)

def print_all_vacancies():
    db_manager = PostgresDBManager()
    try:
        all = db_manager.get_all_vacancies()
    finally:
        db_manager.disconnect()
    print(f"Все вакансии: {all}")

def print_avg_salary():
    db_manager = PostgresDBManager()
    try:
        salary = db_manager.get_avg_salary()
    finally:
        db_manager.disconnect()
    print(f"Средняя зп: {salary}")

def print_with_higher_salary():
    db_manager = PostgresDBManager()
    try:
        salary_max = db_manager.get_vacancies_with_higher_salary()
    finally:
        db_manager.disconnect()
    print(f"Выше средней зп: {salary_max}")

def print_with_keyword():
    db_manager = PostgresDBManager()
    try:
        keyword = db_manager.get_vacancies_with_keyword()
    finally:
        db_manager.disconnect()
    print(keyword)

def run_interation():
    while True:
        print("""Введите ваш запрос:
             1 - Список всех компаний и количество вакансий у каждой компании
             2 - Cписок всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию          
             3 - Средняя зарплата по вакансиям
             4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям
             5 - Список всех вакансий, в названии которых содержатся ключевые слова
             0 - Выйти""")
        user_input = input()

        if user_input == '0':
            break
        elif user_input == '1':
            print_employers()
        elif user_input == '2':
            print_all_vacancies()
        elif user_input == '3':
            print_avg_salary()
        elif user_input == '4':
            print_with_higher_salary()
        elif user_input == '5':
            slovo = str(input('Найти: '))
            print_with_keyword(slovo)

