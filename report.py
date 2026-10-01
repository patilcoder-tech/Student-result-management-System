from tkinter import *
from tkinter import messagebox
import sqlite3


class ReportClass:

    def __init__(self, root):

        self.root = root
        self.root.title("View Result")
        self.root.geometry("1000x600+250+150")
        self.root.config(bg="white")

        self.var_roll = StringVar()
        self.var_id = ""

        # ================= TITLE =================

        Label(
            self.root,
            text="View Student Result",
            font=("Arial", 25, "bold"),
            bg="#033054",
            fg="white"
        ).pack(fill=X)

        # ================= SEARCH SECTION =================

        Label(
            self.root,
            text="Roll No.",
            font=("Arial", 14, "bold"),
            bg="white"
        ).place(x=200, y=80)

        Entry(
            self.root,
            textvariable=self.var_roll,
            font=("Arial", 14),
            bg="lightyellow"
        ).place(x=300, y=80, width=200)

        Button(
            self.root,
            text="Search",
            font=("Arial", 12, "bold"),
            bg="#03a9f4",
            fg="white",
            command=self.search
        ).place(x=520, y=75, width=100)

        Button(
            self.root,
            text="Clear",
            font=("Arial", 12, "bold"),
            bg="gray",
            fg="white",
            command=self.clear
        ).place(x=630, y=75, width=100)

        # ================= RESULT LABELS =================

        self.labels = []
        y = 150

        for text in ["Roll", "Name", "Course", "Marks", "Total", "Percentage"]:

            Label(
                self.root,
                text=text,
                font=("Arial", 14, "bold"),
                bg="white"
            ).place(x=150, y=y)

            lbl = Label(
                self.root,
                font=("Arial", 14),
                bg="lightgrey"
            )

            lbl.place(x=300, y=y, width=250)

            self.labels.append(lbl)

            y += 50

        # ================= DELETE BUTTON =================

        Button(
            self.root,
            text="Delete",
            font=("Arial", 12, "bold"),
            bg="red",
            fg="white",
            command=self.delete
        ).place(x=380, y=490, width=120)

    # ================= SEARCH =================

    def search(self):

        if self.var_roll.get() == "":

            messagebox.showerror(
                "Error",
                "Enter Roll Number"
            )

            return

        con = sqlite3.connect("student_result.db")
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM result WHERE roll=?",
            (self.var_roll.get(),)
        )

        row = cur.fetchone()

        if row:

            self.var_id = row[0]

            try:

                marks = float(row[4])
                total = float(row[5])

            except:

                messagebox.showerror(
                    "Error",
                    "Invalid Data"
                )

                return

            per = (marks / total) * 100 if total != 0 else 0

            data = [
                row[1],
                row[2],
                row[3],
                marks,
                total,
                f"{per:.2f}%"
            ]

            for i in range(len(self.labels)):

                self.labels[i].config(text=data[i])

        else:

            messagebox.showerror(
                "Error",
                "No Record Found"
            )

            self.clear()

        con.close()

    # ================= CLEAR =================

    def clear(self):

        self.var_roll.set("")
        self.var_id = ""

        for lbl in self.labels:

            lbl.config(text="")

    # ================= DELETE =================

    def delete(self):

        if self.var_id == "":

            messagebox.showerror(
                "Error",
                "Search Record First"
            )

            return

        op = messagebox.askyesno(
            "Confirm",
            "Do you want to delete this record?"
        )

        if op:

            con = sqlite3.connect("student_result.db")
            cur = con.cursor()

            cur.execute(
                "DELETE FROM result WHERE rid=?",
                (self.var_id,)
            )

            con.commit()
            con.close()

            messagebox.showinfo(
                "Success",
                "Record Deleted Successfully"
            )

            self.clear()


# ================= MAIN =================

if __name__ == "__main__":

    root = Tk()

    obj = ReportClass(root)

    root.mainloop()