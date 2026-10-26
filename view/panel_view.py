import tkinter as tk
from view.student_view import StudentView

class PanelView:
    def students_click(self):
        student_ui = StudentView()

    def __init__(self):
        self.win=tk. Tk()
        self.win.geometry("300x200")
        self.win.title(" سیستم مدیریت کلاسی")

        self.btn_student= tk.Button(self.win, text="مدیریت دانش آموزان" , command=self.students_click)
        self.btn_student.place(x=90, y=60)

        self.win.mainloop()

if __name__=="__main__":
    app=PanelView()