import tkinter as tk
from tkinter import messagebox
from controller.grade_controller import GradeController

class GradeView:
    def __init__(self):
        self.grade_controller = GradeController()

        self.window= tk.Tk()
        self.window.title("ثبت نمره دانش آموز")
        self.window.geometry("400x320")

        self.lbl_national_id=tk.Label(self.window, text="کد ملی دانش آموز:")
        self.lbl_national_id.place(x=250, y=30)
        self.ent_national_id=tk.Entry(self.window, justify="right")
        self.ent_national_id.place(x=80, y=30)

        self.lbl_lesson=tk.Label(self.window, text="نام درس:")
        self.lbl_lesson.place(x=250, y=85)
        self.ent_lesson=tk.Entry(self.window, justify="right")
        self.ent_lesson.place(x=80, y=85)

        self.lbl_score=tk.Label(self.window,text="نمره: ")
        self.lbl_score.place(x=250, y=140)
        self.ent_score=tk.Entry(self.window, justify="right")
        self.ent_score.place(x=80, y=140)

        self.btn_save=tk.Button(self.window,text="ثبت نمره" , command=self.save_grade)
        self.btn_save.place(x=150, y=210)

    def save_grade(self):
        national_id=self.ent_national_id.get()
        lesson=self.ent_lesson.get()
        score=self.ent_score.get()

        status_bool, message= self.grade_controller.save(national_id,lesson , score)

        if status_bool:
            messagebox.showinfo( "موفقیت", message )
            self.ent_national_id.delete(0, tk.END)
            self.ent_lesson.delete(0, tk.END)
            self.ent_score.delete(0, tk.END)
        else:
            messagebox.showerror("خطا", message )

    def run(self):
        self.window.mainloop()

if __name__=="__main__":
    app = GradeView()
    app.run()
