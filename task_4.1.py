# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

# Решение

import sqlite3

# Создание таблицы Школы
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE Schools (
School_Id INTEGER NOT NULL PRIMARY KEY,
School_Name TEXT NOT NULL);"""
cursor.execute(query)
connection.commit()
connection.close()

import sqlite3

# Наполнение таблицы Школы
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO School (School_Id , School_Name ,)
VALUES
('1', 'Начальная'),
('2', 'Средняя'),
('3', 'Колледж'),
('4', 'Высшая');"""
cursor.execute(query)
connection.commit()
connection.close()

import sqlite3

# Создание таблицы Студенты
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL, PRIMARY KEY,
);"""
cursor.execute(query)
connection.commit()
connection.close()

import sqlite3

# Наполнение таблицы Студенты
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO Student (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4');"""
cursor.execute(query)
connection.commit()
connection.close()

# Подключиться к БД и вывод ее версии

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def read_database_version():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()
    print (version)
    close_connection(connection)
    print ("Вы подключись к версии Sqlite: ", version)
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

read_database_version()

# Информация о школе и студенте

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Schools WHERE School_Id = ?"
    cursor.execute(query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

def get_Student_data(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Students WHERE School_Id = ?"
    cursor.execute(query,(school_id,))
    records = cursor.fetchall()
    for row in records:
      print ("ID студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", get_school_name(row[2]), "\n")
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

get_Student_data(1)
