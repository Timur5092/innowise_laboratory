import sqlite3

# Создаём базу
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Загружаем schema.sql
with open("schema.sql", "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

# Загружаем data.sql
with open("data.sql", "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()

print("База данных успешно создана и заполнена!")

