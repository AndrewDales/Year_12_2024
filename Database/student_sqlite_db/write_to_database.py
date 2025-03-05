# write_to_student_db.py
import sqlite3
from faker import Faker
import random

# Example - parameterized query
parameterised_insert_query = """
INSERT INTO 
    students (first_name, last_name, age, gender)
VALUES
    (?, ?, ?, ?);
"""

fake = Faker('en_GB')
fake.random.seed(4321)

data = [(fake.first_name(), fake.last_name(),
         random.randint(11, 18),
         random.choice(('male', 'female')))
        for _ in range(100)]

# Create a connection to the database
with sqlite3.connect("student.sqlite") as conn:
    # Create a cursor
    cursor = conn.cursor()
    cursor.executemany(parameterised_insert_query, data)
