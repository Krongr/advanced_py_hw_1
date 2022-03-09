from datetime import date
from application import salary
from application.db import people


if __name__ == "__main__":
    print(f'Greetings, today is {date.today()}')
    people.get_employees()
    salary.calculate_salary()