import tkinter as tk
from tkinter import messagebox
from controller.attendance_controller import AttendanceController

class AttendanceView:
    def __init__(self):
        self.attendance_controller = AttendanceController()

        self.window = tk.Tk()
        self.window.title("ثبت حضور و غیاب")
        self.window.geometry("400x350")

        self.lbl_national_id=tk.Label(self.window, text="کد ملی دانش آموز: ")
        self.lbl_national_id.place(x=250,y=30)
        self.ent_national_id=tk.Entry(self.window, justify="right")
        self.ent_national_id.place(x=80,y=30)

        self.lbl_date=tk.Label(self.window,text="تاریخ :")
        self.lbl_date.place(x=250,y=80)
        self.ent_date=tk.Entry(self.window, justify="right")
        self.ent_date.place(x=80,y=80)

        self.lbl_date=tk.Label(self.window, text=" وضعیت(حاضر/غایب): ")
        self.lbl_date.place(x=250,y=130)
        self.ent_status=tk.Entry(self.window, justify="right")
        self.ent_status.place(x=80,y=130)

        self.bth_save=tk.Button(self.window, text="ثبت حضور و غیاب" , command=self.save_attendance)
        self.bth_save.place(x=150,y=190)

    def save_attendance(self):
        national_id = self.ent_national_id.get()
        date = self.ent_date.get()
        status= self.ent_status.get()

        status_bool, message= self.attendance_controller.save(national_id, date, status,"")

        if status_bool:
            messagebox.showinfo("موفقیت" , message )
            self.ent_national_id.delete(0, tk.END)
            self.ent_date.delete(0, tk.END)
            self.ent_status.delete(0, tk.END)

        else:
            messagebox.showerror("خطا" , message )

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = AttendanceView()
    app.run()