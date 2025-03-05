import sqlite3

with sqlite3.connect('student.sqlite') as conn:
    cur = conn.cursor()
    group_by_sql = """
    select substr(first_name, 1, 1), sum(age)
    from students
    group by substr(first_name, 1, 1);"""

    sum_ages = cur.execute(group_by_sql).fetchall()
