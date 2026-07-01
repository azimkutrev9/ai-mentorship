import requests
import sqlite3

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    user_name = data[0]["name"]
    user_email = data[0]["email"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()  # Курсорът е обектът, който изпълнява SQL командите

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)

    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user_name, user_email))
    conn.commit()

    conn.close()

    print(f"Потребителят {user_name} е успешно записан в базата данни!")