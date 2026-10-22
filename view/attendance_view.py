import tkinter as tk
from tkinter import messagebox
from controller.attendance_controller import AttendanceController

class AttendanceView:
    def __init__(self):
        self.attendance_controller = AttendanceController()

        self.window = tk.Tk()
        self.window.title("ثبت حضور و غیاب")
        self.window.geometry("400x300")

        self.lbl_national_id=tk.Label(self.window, text="کد ملی دانش آموز: ")
        self.lbl_national_id.place(x=250,y=30)
        self.ent_national_id=tk.Entry(self.window, justify"right")
        self.ent_national_id.place(x=80,y=30)

        