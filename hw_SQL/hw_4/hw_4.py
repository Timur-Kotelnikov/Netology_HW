import psycopg2
from config import host, user, password, db_name, port


def create_tables():
    return f"CREATE TABLE IF NOT EXISTS customers (customer_id INT PRIMARY KEY, first_name VARCHAR (50), last_name " \
           f"VARCHAR (50), email VARCHAR(50)); CREATE TABLE IF NOT EXISTS phones (phone_number VARCHAR (20) PRIMARY " \
           f"KEY, customer_id INT REFERENCES customers(customer_id));"


def add_customer():
    customer_id = input('customer_id: ')
    first_name = input('first_name: ')
    last_name = input('last_name: ')
    email = input('email: ')
    return f"INSERT INTO customers (customer_id, first_name, last_name, email) VALUES ('{customer_id}', " \
           f"'{first_name}', '{last_name}', '{email}');"


def add_phone():
    customer_id = input('customer_id: ')
    phone_number = input('phone_number: ')
    return f"INSERT INTO phones (phone_number, customer_id) VALUES ('{phone_number}', '{customer_id}')"


def update_customer():
    customer_id = input('customer_id: ')
    data_name = input('data to update: ')
    new_data = input('new data: ')
    return f"UPDATE customers SET {data_name} = '{new_data}' where customer_id = '{customer_id}';"


def delete_phone():
    phone_number = input('phone_number: ')
    return f"DELETE FROM phones where phone_number = '{phone_number}';"


def delete_customer():
    customer_id = input('customer_id: ')
    return f"DELETE FROM phones where customer_id = '{customer_id}';" \
           f"DELETE FROM customers where customer_id = '{customer_id}';"


def search_customer():
    data_type = input('data type: ')
    customer_data = input('data: ')
    return f"SELECT first_name, last_name FROM customers where {data_type} = '{customer_data}';"


def call_function(function):
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=db_name, port=port)
        with connection.cursor() as cursor:
            cursor.execute(function)
            connection.commit()
            try:
                a = cursor.fetchone()
                return f'{a[0]} {a[1]}'
            except Exception:
                pass
    except Exception as _ex:
        print('Error!', _ex)
    finally:
        if connection:
            connection.close()
