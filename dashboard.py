from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# IMPORT FILES
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass


class RMS:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1600x1200+0+0")
        self.root.config(bg="white")

        # ================= TITLE =================

        title = Label(
            self.root,
            text="Student Result Management System",
            font=("goudy old style", 30, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=70)

        # ================= MENU FRAME =================

        M_Frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15),
            bg="white"
        )
        M_Frame.place(x=10, y=80, width=1330, height=80)

        # ================= BUTTONS =================

        btn_course = Button(
            M_Frame,
            text="Course",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_course
        )
        btn_course.place(x=20, y=10, width=180, height=40)

        btn_student = Button(
            M_Frame,
            text="Student",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_student
        )
        btn_student.place(x=230, y=10, width=180, height=40)

        btn_result = Button(
            M_Frame,
            text="Add Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_result
        )
        btn_result.place(x=440, y=10, width=180, height=40)

        btn_report = Button(
            M_Frame,
            text="View Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_report
        )
        btn_report.place(x=650, y=10, width=180, height=40)

        btn_exit = Button(
            M_Frame,
            text="Exit",
            font=("goudy old style", 15, "bold"),
            bg="red",
            fg="white",
            cursor="hand2",
            command=self.exit_app
        )
        btn_exit.place(x=860, y=10, width=180, height=40)

        # ================= BACKGROUND IMAGE =================

        try:

            self.bg_img = Image.open("Images/main.jpeg")

            self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)

            self.bg_img = ImageTk.PhotoImage(self.bg_img)

            bg = Label(self.root, image=self.bg_img, bd=0)

            bg.place(x=750, y=250, width=720, height=550)

        except Exception as ex:

            print("Image Error :", ex)

            bg = Label(
                self.root,
                text="Image Not Found",
                font=("goudy old style", 40, "bold"),
                bg="white",
                fg="red"
            )

            bg.place(x=200, y=250, width=920, height=100)

        # ================= FOOTER =================

        footer = Label(
            self.root,
            text="SRMS - Student Result Management System\nDeveloped in Python using Tkinter",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white"
        )

        footer.pack(side=BOTTOM, fill=X)

    # ================= FUNCTIONS =================

    def add_course(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_report(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def exit_app(self):

        op = messagebox.askyesno(
            "Exit",
            "Do you really want to exit?"
        )

        if op:
            self.root.destroy()


# ================= MAIN =================

if __name__ == "__main__":

    root = Tk()

    obj = RMS(root)

    root.mainloop()