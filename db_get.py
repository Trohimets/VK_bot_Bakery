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


connection = create_connection("db.sqlite")


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


def select_products(category):
    select_products = f"SELECT name from products JOIN categories ON Products.category = Categories.id WHERE type = '{category}'"
    items = execute_read_query(connection, select_products)
    products = []
    for i in range(len(items)):
        products += items[i]
    return products


def select_categories():
    select_categories = "SELECT type from categories"
    items = execute_read_query(connection, select_categories)
    categories = []
    for i in range(len(items)):
        categories += items[i]
    return categories


def select_product(product):
    select_product = f"SELECT description, image from products WHERE name = '{product}'"
    items = execute_read_query(connection, select_product)
    product = []
    for i in range(len(items)):
        product += items[i]
    return product


def select_all_products():
    select_products = "SELECT name from products"
    items = execute_read_query(connection, select_products)
    products = []
    for i in range(len(items)):
        products += items[i]
    return products
