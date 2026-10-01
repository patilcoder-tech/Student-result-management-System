from tkinter import *
from tkinter import messagebox
import sqlite3


class ResultClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1000x550+200+250")
        self.root.config(bg="white")

        # VARIABLES
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_total = StringVar()

        # TITLE
        Label(self.root, text="Manage Student Result",
              font=("Arial", 25, "bold"),
              bg="#033054", fg="white").pack(fill=X)

        # SEARCH FRAME
        Label(self.root, text="Enter Roll No",
              font=("Arial", 14, "bold"),
              bg="white").place(x=100, y=100)

        Entry(self.root, textvariable=self.var_roll,
              font=("Arial", 14),
              bg="lightyellow").place(x=250, y=100, width=200)

        Button(self.root, text="Search",
               font=("Arial", 14, "bold"),
               bg="#03a9f4", fg="white",
               command=self.search).place(x=500, y=95, width=120)

        # DETAILS
        Label(self.root, text="Name", font=("Arial", 14, "bold"),
              bg="white").place(x=100, y=180)

        Entry(self.root, textvariable=self.var_name,
              font=("Arial", 14), state="readonly").place(x=250, y=180, width=250)

        Label(self.root, text="Course", font=("Arial", 14, "bold"),
              bg="white").place(x=550, y=180)

        Entry(self.root, textvariable=self.var_course,
              font=("Arial", 14), state="readonly").place(x=650, y=180, width=250)

        # MARKS
        Label(self.root, text="Marks", font=("Arial", 14, "bold"),
              bg="white").place(x=100, y=260)

        Entry(self.root, textvariable=self.var_marks,
              font=("Arial", 14),
              bg="lightyellow").place(x=250, y=260, width=250)

        Label(self.root, text="Total", font=("Arial", 14, "bold"),
              bg="white").place(x=550, y=260)

        Entry(self.root, textvariable=self.var_total,
              font=("Arial", 14),
              bg="lightyellow").place(x=650, y=260, width=250)

        # BUTTONS
        Button(self.root, text="Add Result",
               font=("Arial", 14, "bold"),
               bg="green", fg="white",
               command=self.add).place(x=300, y=350, width=150)

        Button(self.root, text="Clear",
               font=("Arial", 14, "bold"),
               bg="gray", fg="white",
               command=self.clear).place(x=500, y=350, width=150)

        self.create_db()

    # ================= DATABASE =================
    def create_db(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS student(
                roll TEXT PRIMARY KEY,
                name TEXT,
                course TEXT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS result(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                roll TEXT,
                name TEXT,
                course TEXT,
                marks REAL,
                total REAL
            )
        """)

        con.commit()
        con.close()

    # ================= SEARCH =================
    def search(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        cur.execute("SELECT name, course FROM student WHERE roll=?",
                    (self.var_roll.get(),))

        row = cur.fetchone()

        if row:
            self.var_name.set(row[0])
            self.var_course.set(row[1])
        else:
            messagebox.showerror("Error", "Student Not Found")

        con.close()

    # ================= ADD =================
    def add(self):

        if self.var_roll.get() == "" or self.var_marks.get() == "" or self.var_total.get() == "":
            messagebox.showerror("Error", "All fields required")
            return

        try:
            marks = float(self.var_marks.get())
            total = float(self.var_total.get())

            con = sqlite3.connect("student_result.db")
            cur = con.cursor()

            cur.execute("""
                INSERT INTO result(roll,name,course,marks,total)
                VALUES(?,?,?,?,?)
            """, (
                self.var_roll.get(),
                self.var_name.get(),
                self.var_course.get(),
                marks,
                total
            ))

            con.commit()
            con.close()

            messagebox.showinfo("Success", "Result Added")
            self.clear()

        except:
            messagebox.showerror("Error", "Invalid Input")

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_total.set("")


# RUN
if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()