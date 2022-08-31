import sqlite3
from sqlite3 import Error


#Подключение к БД
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("D:\dev\VK_bot_Bakery\db.sqlite")

#Функция создания таблицы в БД
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#Запрос на создание таблицы Категории
create_categories_table = """
CREATE TABLE IF NOT EXISTS categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT NOT NULL
);
""" 
#Запрос на создание записей в таблице Категории
create_categories = """
INSERT INTO
  categories (type)
VALUES
  ('Торты'),
  ('Выпечка'),
  ('Хлеб');
"""
#Запрос на создание таблицы Продукты
create_products_table = """
CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  image TEXT NOT NULL,
  category INT,
  FOREIGN KEY (category) REFERENCES Categories (id) 
        ON DELETE RESTRICT ON UPDATE CASCADE
);
""" 
#Запрос на создание записей в таблице Продукты
create_products = """
INSERT INTO
  Products (name, description, image, category)
VALUES
  ("Клубничный пирог", "Свежие ягоды", 'link to image', 2),
  ("Малиновый пай", "Диетическое тесто", 'link to image', 2),
  ("Осетинский пирог", "С бараниной", 'link to image', 2),
  ("Торт Наполеон", "Настоящее масло", 'link to image', 1),
  ("Торт Чизкейк", "С сыром Маскарпоне", 'link to image', 1),
  ("Торт Сметанник", "Только самая свежая сметана", 'link to image', 1),
  ("Хлеб Бородинский", "ржаной", 'link to image', 3),
  ("Батон Семейный", "пышное тесто", 'link to image', 3),
  ("Хлеб Мариинский", "с изюмом и кориандром", 'link to image', 3);
"""

#Создаем 2 таблицы в БД, Категории и Продукты:
execute_query(connection, create_categories_table)  
execute_query(connection, create_products_table)  

#Создаем в таблицах записи:
execute_query(connection, create_categories) 
execute_query(connection, create_products)  

