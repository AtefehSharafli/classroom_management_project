import tkinter as tk
from tkinter import messagebox
from controller.lesson_controller import LessonController

class LessonView:
    def __init__(self):
        self.lesson_controller = LessonController()
#ساخت پنجره اصلی مدیریت درس ها
        self.window = tk.Tk()
        self.window.title("مدیریت درس ها")
        self.window.geometry("400x300")
#برچسب و کادر ورودی نام درس
        self.lbl_name=tk.Label(self.window, text="نام درس: ")
        self.lbl_name.place(x=250, y=40)
        self.ent_name=tk.Entry(self.window, justify="right")
        self.ent_name.place(x=80, y=40)
#برچسب و کادر ورودی تعداد واحد
        self.lbl_unit=tk.Label(self.window, text="تعداد واحد: ")
        self.lbl_unit.place(x=250, y=100)
        self.ent_unit=tk.Entry(self.window, justify="right")
        self.ent_unit.place(x=80, y=100)
#دکمه ثبت درس
        self.btn_save=tk.Button(self.window, text= "ثبت درس" , command=self.save_lesson)
        self.btn_save.place(x=160, y=180)
#خواندن اطلاعات و ذخیره کردن درس
    def save_lesson(self):
        name = self.ent_name.get()
        unit = self.ent_unit.get()
#ارسال اطلاعات به کنترلر برای ذخیره سازی
        status_bool, message=self.lesson_controller.save(name, unit)
#اگر ذخیره موفقیت آمیز بود پیام موفقیت بده و کادر ها رو خالی کن
        if status_bool:
            messagebox.showinfo("موفقیت", message)
            self.ent_name.delete(0, tk.END)
            self.ent_unit.delete(0, tk.END)
#اگر خطا داشت پیام خطا نشون بده
        else:
            messagebox.showerror("خطا", message)
#اجرای پنجره گرافیکی
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = LessonView()
    app.run()