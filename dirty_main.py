from datetime import *
from application.db.people import *
from application.salary import *


if __name__ == "__main__":
    print(f'Greetings, today is {date.today()}')
    get_employees()
    calculate_salary()