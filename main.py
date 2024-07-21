from kurs5.api_clients import HeadHunterAPIClient
from kurs5.config import settings
from kurs5.db.loader import load_employers, load_vacancies
from kurs5.db.migrations import create_database, apply_migrations
from prettytable import PrettyTable

def main():

    print("""Введите ваш запрос:
              1 - Список всех компаний и количество вакансий у каждой компании
              2 - Cписок всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию          
              3 - Средняя зарплата по вакансиям
              4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям
              5 - Список всех вакансий, в названии которых содержатся ключевые слова""")



if __name__ == '__main__':
    main()
