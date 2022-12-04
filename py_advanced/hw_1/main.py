from application.salary import calculate_salary as salary_list
import datetime

if __name__ == '__main__':
    print(f'Today is {datetime.date.today()}')
    print(salary_list())