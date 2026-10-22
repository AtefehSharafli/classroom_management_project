from tkinter import *
from view.student_view import StudentView

class PanelView:
    def students_click(self):
        student_ui = StudentView()

    def __init__(self):
        self.win=Tk()
        self.win.geometry("300x200")
        self.win.title(" سیستم مدیریت کلاسی")

        Button(self.win, text="مدیریت دانش آموزان", command=self.students_click, width=20).place(x=70,y=60)

        self.win.mainloop()