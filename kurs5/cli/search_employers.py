from kurs5.api_clients import HeadHunterAPIClient
from prettytable import PrettyTable

hh_client = HeadHunterAPIClient()

def run():
    print('Введите текст для поиска работодателя')
    search = input()
    employers = hh_client.search_employers(search)
    if not employers:
        print('По данному запросу ничего не найдено')
        return

    table = PrettyTable(field_names=['ID', 'Название компании', 'Ссылка', 'Количество вакансий'])
    for emp in employers:
        table.add_row([emp.id, emp.name, emp.url, emp.open_vacancies])

    print(f'Найдено {len(employers)} компаний')
    print(table)


if __name__ == '__main__':
    run()