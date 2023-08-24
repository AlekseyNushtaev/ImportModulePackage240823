from datetime import *
from dateparser import *
from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    text = '12 апреля 1961 года'
    print(f'Date of flight Gagarin -', parse(text).date())
    print(f'Today is', datetime.now().date())
    calculate_salary()
    get_employees()