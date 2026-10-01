from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class StudentClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1500x900+60+100")
        self.root.config(bg="white")

        # ================= VARIABLES =================

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_admission = StringVar()
        self.var_course = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        # ================= TITLE =================

        title = Label(
            self.root,
            text="Manage Student Details",
            font=("goudy old style", 30, "bold"),
            bg="#033054",
            fg="white",
            anchor="w"
        )

        title.place(x=0, y=15, relwidth=1, height=50)

        # ================= LABELS =================

        Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=100)
        Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=160)
        Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=220)
        Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=280)
        Label(self.root, text="DOB", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=340)

        Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=100)
        Label(self.root, text="Admission Date", font=("goudy old style", 15, "bold"), bg="white").place(x=480, y=160)
        Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=220)
        Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=280)
        Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=340)
        Label(self.root, text="Pin Code", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=400)
        Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=50, y=450)

        # ================= ENTRIES =================

        Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=100, width=250)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=160, width=250)

        Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=220, width=250)

        cmb_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("Select", "Male", "Female", "Other"),
            state='readonly',
            justify=CENTER,
            font=("goudy old style", 15)
        )

        cmb_gender.place(x=180, y=280, width=250)
        cmb_gender.current(0)

        Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=340, width=250)

        Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=650, y=100, width=250)

        Entry(self.root, textvariable=self.var_admission, font=("goudy old style", 15), bg="lightyellow").place(x=650, y=160, width=250)

        Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="lightyellow").place(x=650, y=220, width=250)

        Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg="lightyellow").place(x=650, y=280, width=250)

        Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15), bg="lightyellow").place(x=650, y=340, width=250)

        Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15), bg="lightyellow").place(x=650, y=400, width=250)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=180, y=460, width=720, height=100)

        # ================= BUTTONS =================

        Button(
            self.root,
            text="Save",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add
        ).place(x=180, y=590, width=120, height=40)

        Button(
            self.root,
            text="Update",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.update
        ).place(x=320, y=590, width=120, height=40)

        Button(
            self.root,
            text="Delete",
            font=("goudy old style", 15, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete
        ).place(x=460, y=590, width=120, height=40)

        Button(
            self.root,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="gray",
            fg="white",
            cursor="hand2",
            command=self.clear
        ).place(x=600, y=590, width=120, height=40)

        # ================= TABLE FRAME =================

        frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame.place(x=930, y=100, width=540, height=500)

        scrolly = Scrollbar(frame, orient=VERTICAL)
        scrollx = Scrollbar(frame, orient=HORIZONTAL)

        self.StudentTable = ttk.Treeview(
            frame,
            columns=(
                "roll", "name", "email", "gender", "dob",
                "contact", "admission", "course", "state",
                "city", "pin", "address"
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        self.StudentTable.heading("roll", text="Roll No")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("dob", text="DOB")
        self.StudentTable.heading("contact", text="Contact")
        self.StudentTable.heading("admission", text="Admission")
        self.StudentTable.heading("course", text="Course")
        self.StudentTable.heading("state", text="State")
        self.StudentTable.heading("city", text="City")
        self.StudentTable.heading("pin", text="Pin")
        self.StudentTable.heading("address", text="Address")

        self.StudentTable["show"] = "headings"

        self.StudentTable.pack(fill=BOTH, expand=1)

        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)

        self.create_table()
        self.show()

    # ================= CREATE TABLE =================

    def create_table(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

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

        con.commit()
        con.close()

    # ================= ADD =================

    def add(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        try:

            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No is required")

            else:

                cur.execute(
                    "SELECT * FROM student WHERE roll=?",
                    (self.var_roll.get(),)
                )

                row = cur.fetchone()

                if row is not None:

                    messagebox.showerror(
                        "Error",
                        "Roll No already exists"
                    )

                else:

                    cur.execute(
                        "INSERT INTO student VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_admission.get(),
                            self.var_course.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_pin.get(),
                            self.txt_address.get("1.0", END)
                        )
                    )

                    con.commit()

                    messagebox.showinfo(
                        "Success",
                        "Student Added Successfully"
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

            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()

            self.StudentTable.delete(*self.StudentTable.get_children())

            for row in rows:
                self.StudentTable.insert('', END, values=row)

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to : {str(ex)}"
            )

        finally:

            con.close()

    # ================= GET DATA =================

    def get_data(self, ev):

        f = self.StudentTable.focus()
        content = self.StudentTable.item(f)
        row = content['values']

        if row:

            self.var_roll.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_admission.set(row[6])
            self.var_course.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])

            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, row[11])

    # ================= UPDATE =================

    def update(self):

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        try:

            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error",
                    "Roll Number Required"
                )

            else:

                cur.execute(
                    """
                    UPDATE student SET
                    name=?,
                    email=?,
                    gender=?,
                    dob=?,
                    contact=?,
                    admission=?,
                    course=?,
                    state=?,
                    city=?,
                    pin=?,
                    address=?
                    WHERE roll=?
                    """,
                    (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_admission.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get()
                    )
                )

                con.commit()

                messagebox.showinfo(
                    "Success",
                    "Student Updated Successfully"
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

            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error",
                    "Select Student First"
                )

            else:

                op = messagebox.askyesno(
                    "Confirm",
                    "Do you really want to delete?"
                )

                if op:

                    cur.execute(
                        "DELETE FROM student WHERE roll=?",
                        (self.var_roll.get(),)
                    )

                    con.commit()

                    messagebox.showinfo(
                        "Delete",
                        "Student Deleted Successfully"
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

    # ================= CLEAR =================

    def clear(self):

        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_admission.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.var_search.set("")

        self.txt_address.delete("1.0", END)

        self.show()


# ================= MAIN =================

if __name__ == "__main__":

    root = Tk()
    obj = StudentClass(root)
    root.mainloop()