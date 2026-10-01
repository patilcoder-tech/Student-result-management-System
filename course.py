from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class CourseClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1500x800+60+220")
        self.root.config(bg="white")

        # ================= VARIABLES =================

        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        # ================= TITLE =================

        title = Label(
            self.root,
            text="Manage Course Details",
            font=("goudy old style", 30, "bold"),
            bg="#033054",
            fg="white",
            anchor="w"
        )

        title.place(x=0, y=15, relwidth=1, height=50)

        # ================= LABELS =================

        Label(
            self.root,
            text="Course Name",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=100)

        Label(
            self.root,
            text="Duration",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=160)

        Label(
            self.root,
            text="Charges",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=220)

        Label(
            self.root,
            text="Description",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=280)

        # ================= ENTRY BOXES =================

        self.txt_courseName = Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15),
            bg="lightyellow"
        )

        self.txt_courseName.place(x=220, y=100, width=300)

        txt_duration = Entry(
            self.root,
            textvariable=self.var_duration,
            font=("goudy old style", 15),
            bg="lightyellow"
        )

        txt_duration.place(x=220, y=160, width=300)

        txt_charges = Entry(
            self.root,
            textvariable=self.var_charges,
            font=("goudy old style", 15),
            bg="lightyellow"
        )

        txt_charges.place(x=220, y=220, width=300)

        # ================= DESCRIPTION =================

        self.text_description = Text(
            self.root,
            font=("goudy old style", 15),
            bg="lightyellow"
        )

        self.text_description.place(x=220, y=280, width=500, height=120)

        # ================= BUTTONS =================

        Button(
            self.root,
            text="Save",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add
        ).place(x=220, y=430, width=120, height=40)

        Button(
            self.root,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="gray",
            fg="white",
            cursor="hand2",
            command=self.clear
        ).place(x=360, y=430, width=120, height=40)

        Button(
            self.root,
            text="Update",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.update
        ).place(x=500, y=430, width=120, height=40)

        Button(
            self.root,
            text="Delete",
            font=("goudy old style", 15, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete
        ).place(x=640, y=430, width=120, height=40)

        # ================= SEARCH =================

        Label(
            self.root,
            text="Course Name",
            font=("goudy old style", 18, "bold"),
            bg="white"
        ).place(x=790, y=70)

        txt_search = Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 15),
            bg="lightyellow"
        )

        txt_search.place(x=980, y=75, width=180)

        Button(
            self.root,
            text="Search",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.search
        ).place(x=1180, y=75, width=120, height=35)

        # ================= TABLE FRAME =================

        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.C_Frame.place(x=840, y=170, width=620, height=390)

        # ================= SCROLLBAR =================

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        # ================= TREEVIEW =================

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=("cid", "name", "duration", "charges", "description"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")

        self.CourseTable["show"] = "headings"

        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=150)
        self.CourseTable.column("duration", width=150)
        self.CourseTable.column("charges", width=150)
        self.CourseTable.column("description", width=300)

        self.CourseTable.pack(fill=BOTH, expand=1)

        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        # ================= DATABASE =================

        self.create_table()
        self.show()

    # ================= CREATE TABLE =================

    def create_table(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS course(
                cid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        """)

        con.commit()
        con.close()

    # ================= ADD =================

    def add(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        try:

            if self.var_course.get() == "":

                messagebox.showerror(
                    "Error",
                    "Course Name is required",
                    parent=self.root
                )

            else:

                cur.execute(
                    "SELECT * FROM course WHERE name=?",
                    (self.var_course.get(),)
                )

                row = cur.fetchone()

                if row is not None:

                    messagebox.showerror(
                        "Error",
                        "Course already available",
                        parent=self.root
                    )

                else:

                    cur.execute(
                        "INSERT INTO course(name,duration,charges,description) VALUES(?,?,?,?)",
                        (
                            self.var_course.get(),
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.text_description.get("1.0", END)
                        )
                    )

                    con.commit()

                    messagebox.showinfo(
                        "Success",
                        "Course Added Successfully",
                        parent=self.root
                    )

                    self.show()
                    self.clear()

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to : {str(ex)}"
            )

        finally:
            con.close()

    # ================= SHOW =================

    def show(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        try:

            cur.execute("SELECT * FROM course")

            rows = cur.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
                self.CourseTable.insert('', END, values=row)

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to : {str(ex)}"
            )

        finally:
            con.close()

    # ================= GET DATA =================

    def get_data(self, ev):

        f = self.CourseTable.focus()
        content = self.CourseTable.item(f)

        row = content['values']

        if row:

            self.var_course.set(row[1])
            self.var_duration.set(row[2])
            self.var_charges.set(row[3])

            self.text_description.delete("1.0", END)
            self.text_description.insert(END, row[4])

    # ================= UPDATE =================

    def update(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        try:

            cur.execute(
                "UPDATE course SET duration=?,charges=?,description=? WHERE name=?",
                (
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.text_description.get("1.0", END),
                    self.var_course.get()
                )
            )

            con.commit()

            messagebox.showinfo(
                "Success",
                "Course Updated Successfully",
                parent=self.root
            )

            self.show()

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to : {str(ex)}"
            )

        finally:
            con.close()

    # ================= DELETE =================

    def delete(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        try:

            op = messagebox.askyesno(
                "Confirm",
                "Do you really want to delete?",
                parent=self.root
            )

            if op:

                cur.execute(
                    "DELETE FROM course WHERE name=?",
                    (self.var_course.get(),)
                )

                con.commit()

                messagebox.showinfo(
                    "Delete",
                    "Course Deleted Successfully",
                    parent=self.root
                )

                self.show()
                self.clear()

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to : {str(ex)}"
            )

        finally:
            con.close()

    # ================= SEARCH =================

    def search(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        try:

            cur.execute(
                "SELECT * FROM course WHERE name LIKE ?",
                ('%' + self.var_search.get() + '%',)
            )

            rows = cur.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
                self.CourseTable.insert('', END, values=row)

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to : {str(ex)}"
            )

        finally:
            con.close()

    # ================= CLEAR =================

    def clear(self):

        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")

        self.text_description.delete("1.0", END)


# ================= MAIN =================

if __name__ == "__main__":

    root = Tk()
    obj = CourseClass(root)
    root.mainloop()