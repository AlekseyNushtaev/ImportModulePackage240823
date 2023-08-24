import datetime
import dateparser
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    text = '12 апреля 1961 года'
    print(f'Date of flight Gagarin -', dateparser.parse(text).date())
    print(f'Today is',datetime.datetime.now().date())
    calculate_salary()
    get_employees()
