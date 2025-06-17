import mysql.connector
import requests

def db():
    def words_from_git():
        url = "https://raw.githubusercontent.com/brown-uk/dict_uk/master/dict_uk.txt"
        response = requests.get(url)

        uk_words = response.text.splitlines()

        return uk_words[:20]

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1111",
        database="practice"
    )

    cursor = conn.cursor()

    def table():
        # Таблиця:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS words (
                id INT AUTO_INCREMENT PRIMARY KEY,
                word VARCHAR(255) NOT NULL
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM words")
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.executemany("INSERT INTO words (word) VALUES (%s)", [(w,) for w in words_from_git()])
            conn.commit()
            print("Слова додано у таблицю.")
        else:
            print("Таблиця вже містить дані. Нові слова не додано.")

        cursor.execute("SELECT * FROM words")
        rows = cursor.fetchall()

        word_list = [row[1] for row in rows]
        return word_list