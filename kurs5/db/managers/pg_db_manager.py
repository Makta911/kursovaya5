import psycopg2
from .base import DBManager

class PostgresDBManager(DBManager):
    def connect(self) -> None:
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )

    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_companies_and_vacancies_count(self) -> list[tuple[str, int]]:
        sql = """
            SELECT e.name, COUNT(*) as vacancies_count
            FROM emploters as e
            LEFT JOIN vacancies as v ON e.id = v.employer_id
            GROUP BY e.name
        """
        self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию
        """
        self.cursor.execute("""
            SELECT c.company_name, v.vacancy_name, v.salary_min, v.salary_max, v.vacancy_url
            FROM companies c
            JOIN vacancies v USING(company_id);
        """)
        return self.cursor.fetchall()

    def get_avg_salary(self) -> float:
        sql = """
        SELECT AVG(v.salary_from), AVG(v.salary_to) FROM vacancies as v;
        """
        self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            min_salary, max_salary = cursor.fetchone()
            average_salary = (min_salary + max_salary) / 2
            return round(average_salary, 2)

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        self.cursor.execute("""
               SELECT * FROM vacancies
               WHERE (salary_min + salary_max) > 
               (SELECT AVG(salary_min + salary_max) FROM vacancies);
           """)
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова
        """
        self.cursor.execute("""
               SELECT * FROM vacancies 
               WHERE vacancy_name ILIKE '%%' || %s || '%%';
           """, (keyword,))  # '%%' означает любую последовательность символов перед и после ключевого слова (%s)
        return self.cursor.fetchall()
