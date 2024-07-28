from kurs5.api_clients import HeadHunterAPIClient
from kurs5.config import settings
from kurs5.db.loader import load_employers, load_vacancies
from kurs5.db.migrations import create_database, apply_migrations
from kurs5.user_interaction import run_interation
from prettytable import PrettyTable
from kurs5.db.managers.pg_db_manager import PostgresDBManager
from kurs5.db.managers import pg_db_manager
def main():
    run_interation()


if __name__ == '__main__':
    main()
