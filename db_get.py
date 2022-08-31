import sqlite3
from sqlite3 import Error


# Подключение к БД
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("D:\dev\VK_bot_Bakery\db.sqlite")


# Функция для извлечения данных из БД
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def select_products():
    select_products = "SELECT name from products"
    products = execute_read_query(connection, select_products)
    return products


def select_categories():
    select_categories = "SELECT type from categories"
    categories = execute_read_query(connection, select_categories)
    return categories