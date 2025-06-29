import mysql.connector

def db():
    def words():
        with open("words.txt", "r", encoding="utf-8") as file:
            uk_words = file.read().splitlines()
        return uk_words


    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1111",
        database="practice"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INT AUTO_INCREMENT PRIMARY KEY,
            word VARCHAR(255) NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM words")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("INSERT INTO words (word) VALUES (%s)", [(w,) for w in words()])
        conn.commit()
        print("Слова додано у таблицю.")
    else:
        print("Таблиця вже містить дані. Нові слова не додано.")

    cursor.execute("SELECT * FROM words")
    rows = cursor.fetchall()

    word_list = [row[1] for row in rows]
    return word_list