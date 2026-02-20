import sqlite3
from tabulate import tabulate


conn = sqlite3.connect('students.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade INTEGER,
        city TEXT
    )
''')


cursor.execute('DELETE FROM Students')


students_list = [
    ('Иван', 18, 5, 'Москва'),
    ('Ольга', 19, 4, 'Казань'),
    ('Сергей', 20, 5, 'Самара'),
    ('Мария', 18, 3, 'Омск'),
    ('Анна', 21, 4, 'Тула'),
    ('Павел', 22, 5, 'Пермь'),
    ('Юлия', 20, 3, 'Томск'),
    ('Андрей', 19, 4, 'Сочи'),
    ('Виктор', 18, 5, 'Уфа'),
    ('Светлана', 21, 4, 'Воронеж')
]


cursor.executemany('INSERT INTO Students (name, age, grade, city) VALUES (?, ?, ?, ?)', students_list)
conn.commit()

def show_table(title, query, headers):
    cursor.execute(query)
    data = cursor.fetchall()
    print(f"\n{title}")
    print(tabulate(data, headers=headers, tablefmt="grid", numalign="center", stralign="center"))


show_table("📋 ВСЕ СТУДЕНТЫ", "SELECT * FROM Students", ["ID", "Имя", "Возраст", "Оценка", "Город"])


show_table("⭐ ОЦЕНКА 5", "SELECT name, age, grade, city FROM Students WHERE grade = 5", ["Имя", "Возраст", "Оценка", "Город"])
show_table("👍 ОЦЕНКА 4", "SELECT name, age, grade, city FROM Students WHERE grade = 4", ["Имя", "Возраст", "Оценка", "Город"])
show_table("👎 ОЦЕНКА 3", "SELECT name, age, grade, city FROM Students WHERE grade = 3", ["Имя", "Возраст", "Оценка", "Город"])

conn.close()