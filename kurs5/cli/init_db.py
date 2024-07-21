from kurs5.db.loader import load_employers, load_vacancies
from kurs5.db.migrations import create_database, apply_migrations


def run():
    create_database()
    apply_migrations()
    load_employers()
    load_vacancies()


if __name__ == '__main__':
    run()