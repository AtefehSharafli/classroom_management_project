import tkinter as tk
from tkinter import messagebox
from controller.grade_controller import GradeController

class GradeView:
    def __init__(self):
        self.grade_controller = GradeController()
#ساخت پنچره اصلی ثبت نمره
        self.window= tk.Tk()
        self.window.title("ثبت نمره دانش آموز")
        self.window.geometry("400x320")
#برچسب و کادر ورودی کد ملی دانش آموز
        self.lbl_national_id=tk.Label(self.window, text="کد ملی دانش آموز:")
        self.lbl_national_id.place(x=250, y=30)
        self.ent_national_id=tk.Entry(self.window, justify="right")
        self.ent_national_id.place(x=80, y=30)
#برچسب و کادر ورودی نام درس
        self.lbl_lesson=tk.Label(self.window, text="نام درس:")
        self.lbl_lesson.place(x=250, y=85)
        self.ent_lesson=tk.Entry(self.window, justify="right")
        self.ent_lesson.place(x=80, y=85)
#برچسب و کادر ورودی نمره
        self.lbl_score=tk.Label(self.window,text="نمره: ")
        self.lbl_score.place(x=250, y=140)
        self.ent_score=tk.Entry(self.window, justify="right")
        self.ent_score.place(x=80, y=140)
#دکمه ثبت نمره
        self.btn_save=tk.Button(self.window,text="ثبت نمره" , command=self.save_grade)
        self.btn_save.place(x=150, y=210)
#خواندن اطلاعات و ذخیره کردن نمره
    def save_grade(self):
        national_id=self.ent_national_id.get()
        lesson=self.ent_lesson.get()
        score=self.ent_score.get()
#ارسال اطلاعات نمره به کنترلر برای ذخیره سازی
        status_bool, message= self.grade_controller.save(national_id,lesson , score)
#اگر ذخیره موفقیت آمیز بود پیام موفقیت بده و کادرهارو خالی کن
        if status_bool:
            messagebox.showinfo( "موفقیت", message )
            self.ent_national_id.delete(0, tk.END)
            self.ent_lesson.delete(0, tk.END)
            self.ent_score.delete(0, tk.END)
#اگر خطا داشت پیام خطا نشان بده
        else:
            messagebox.showerror("خطا", message )
#اجرای پنجره گرافیکی
    def run(self):
        self.window.mainloop()

if __name__=="__main__":
    app = GradeView()
    app.run()
