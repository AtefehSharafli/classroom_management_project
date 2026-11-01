import tkinter as tk
from tkinter import messagebox
from controller.attendance_controller import AttendanceController

class AttendanceView:
    def __init__(self):
        self.attendance_controller = AttendanceController()
#ساخت پنجره اصلی حضور و غیاب
        self.window = tk.Tk()
        self.window.title("ثبت حضور و غیاب")
        self.window.geometry("400x350")
#برچسب و کادر ورودی کد ملی دانش آموز
        self.lbl_national_id=tk.Label(self.window, text="کد ملی دانش آموز: ")
        self.lbl_national_id.place(x=250,y=30)
        self.ent_national_id=tk.Entry(self.window, justify="right")
        self.ent_national_id.place(x=80,y=30)
#برچسب و کادر ورودی تاریخ
        self.lbl_date=tk.Label(self.window,text="تاریخ :")
        self.lbl_date.place(x=250,y=80)
        self.ent_date=tk.Entry(self.window, justify="right")
        self.ent_date.place(x=80,y=80)
#برچسب و کادر ورودی وضعیت (حاضر/غایب)
        self.lbl_date=tk.Label(self.window, text=" وضعیت(حاضر/غایب): ")
        self.lbl_date.place(x=250,y=130)
        self.ent_status=tk.Entry(self.window, justify="right")
        self.ent_status.place(x=80,y=130)
#دکمه ثبت  حضور و غیاب
        self.bth_save=tk.Button(self.window, text="ثبت حضور و غیاب" , command=self.save_attendance)
        self.bth_save.place(x=150,y=190)
#خواندن اطلاعات و ذخیره کردن حضور و غیاب
    def save_attendance(self):
        national_id = self.ent_national_id.get()
        date = self.ent_date.get()
        status= self.ent_status.get()
#ارسال اطلاعات به کنترلر برای ذخیره سازی
        status_bool, message= self.attendance_controller.save(national_id, date, status,"")
#ااگر ذخیره موفقیت آمیز بود پیام موفقیت بده و کادرها رو خالی کن
        if status_bool:
            messagebox.showinfo("موفقیت" , message )
            self.ent_national_id.delete(0, tk.END)
            self.ent_date.delete(0, tk.END)
            self.ent_status.delete(0, tk.END)
#اگر خطا داشت پیام خطا نشون بده
        else:
            messagebox.showerror("خطا" , message )
#اجرای پنجره گرافیکی
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = AttendanceView()
    app.run()