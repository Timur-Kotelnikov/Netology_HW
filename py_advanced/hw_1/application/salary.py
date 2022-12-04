from application.db.people import get_employees as list_of_employees


def calculate_salary():
    salary_list = dict()
    for employee in list_of_employees():
        salary_list[employee] = '1000 $'
    return salary_list
