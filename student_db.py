import sqlite3
def connect_db():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, age, course):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    conn.close()

def get_all_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows =cur.fetchall()
    conn.close()
    return rows

def update_student(student_id, name, age, course):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET name = ?,age = ?, course = ? WHERE id = ?", (name, age, course, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()