import sqlite3


def create_db():

    con = sqlite3.connect("student_result.db")
    cur = con.cursor()

    # ================= STUDENT TABLE =================

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
            roll TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            admission TEXT,
            course TEXT,
            state TEXT,
            city TEXT,
            pin TEXT,
            address TEXT
        )
    """)

    # ================= RESULT TABLE =================

    cur.execute("""
        CREATE TABLE IF NOT EXISTS result(
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks_obtained TEXT,
            full_marks TEXT,
            percentage TEXT
        )
    """)

    con.commit()
    con.close()

    print("Database Created Successfully")


create_db()