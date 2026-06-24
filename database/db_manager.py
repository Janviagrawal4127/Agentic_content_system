import sqlite3

def save_blog(topic, filename):

    conn = sqlite3.connect("database/blogs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS blogs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        filename TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO blogs(topic, filename) VALUES (?, ?)",
        (topic, filename)
    )

    conn.commit()
    conn.close()