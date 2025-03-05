import sqlite3

conn = sqlite3.connect('student.sqlite')
cur = conn.cursor()

create_student_table = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT
    );
    """

cur.execute(create_student_table)

conn.close()