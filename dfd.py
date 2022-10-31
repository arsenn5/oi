import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)

    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_student(conn, student):
    try:
        sql = '''INSERT INTO students
        (fillname, mark, hobby, birth_date, is_married)
        VALUES (?,?,?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def delete_student(conn, id):
    try:
        sql = '''DELETE FROM students WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id, ))
        conn.commit()
    except Error as e:
        print(e)

def update_student_mark_martial_status(conn, students):
    try:
        sql = '''UPDATE students SET mark = ?, is_married = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, students)
        conn.commit()
    except Error as e:
        print(e)

def select_all_student(conn):
    try:
        sql = '''SELECT * FROM students'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
             print(row)

    except Error as e:
        print(e)



connection = create_connection("""gr_23_3.db""")
connection_students_table = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (200) NOT  NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''

if connection is not None:
    print("Connected successfilly!")
    select_all_student(connection)
    # update_student_mark_martial_status(connection, (15.08, True, 5))
    # delete_student(connection, 3)

    # create_table(connection, connection_students_table)
    # create_student(connection, ("Arsen", 23.34, "IT", "2006-05-31", False))
    # create_student(connection, ("Mark", 23.34, "ert", "2096-05-31", False))
    # create_student(connection, ("Afgdf", 245.34, "rt", "2046-05-31", False))
    print("Done!")