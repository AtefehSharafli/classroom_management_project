from tkinter import *
from tkinter import ttk, messagebox
from unittest import result

from select import select

from controller.student_controller import StudentController
from data_access.student_da import StudentDa


class StudentView:
    def __init__(self):
        self.controller = StudentController()

        self.win=Tk()
        self.win.geometry("700x380")
        self.win.title("مدیریت دانش آموزان")
#فیلد های ورودی فرم
        Label(self.win, text="کد ملی").place(x=20, y=20)
        self.national_id=StringVar()
        Entry(self.win, textvariable=self.national_id).place(x=120, y=20)

        Label(self.win, text="نام").place(x=20, y=60)
        self.first_name = StringVar()
        Entry(self.win, textvariable=self.first_name).place(x=120, y=60)

        Label(self.win, text="نام خانوادگی").place(x=20, y=100)
        self.last_name = StringVar()
        Entry(self.win, textvariable=self.last_name).place(x=120, y=100)

        Label(self.win, text="نام پدر").place(x=120, y=140)
        self.father_name=StringVar()
        Entry(self.win, textvariable=self.father_name).place(x=20, y=140)

        Label(self.win, text="شماره تماس").place(x=20, y=180)
        self.phone = StringVar()
        Entry(self.win, textvariable=self.phone).place(x=120, y=180)

        self.table= ttk.Treeview(self.win, show="headings", columns=[1,2,3,4,5])
        self.table.pack(x=260, y=20)

        self.table.column(1, width=90)
        self.table.column(2, width=80)
        self.table.column(3, width=90)
        self.table.column(4, width=80)
        self.table.column(5, width=90)

        self.table.heading(1, text="کد ملی")
        self.table.heading(2, text="نام")
        self.table.heading(3, text="نام خانوادگی")
        self.table.heading(4, text="نام پدر")
        self.table.heading(5, text="تلفن")

        self.table.bind("<ButtonRelease>", self.table_click )

        Button(self.win, text="ذخیره" , command=self.save_click, width=15).place(x=120, y=230)

        self.reset_from()
        self.win.mainloop()

    def reset_from(self):
        self.national_id.set("")
        self.first_name.set("")
        self.last_name.set("")
        self.father_name.set("")
        self.phone.set("")

        for item in self.table.get_children():
            self.table.delete(item)

        status, result= self.controller.find_all()
        if status:
            for student in result:
                self.table.insert('', 'end', values=student. to_tuple())

    def save_click(self):
        status, message=self.controller.save(
            self.national_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.father_name.get(),
            self.phone.get(),
        )
        if status:
            messagebox.showinfo("موفقیت", message)
            self.reset_from()
        else:
            messagebox.showerror("خطا", message)

    def table_click(self, event):
        selected_id=self.table.focus()
        selected_student=self.table.item(selected_id)["values"]
        if selected_student:
            self.national_id.set(selected_student[0])
            self.first_name.set(selected_student[1])
            self.last_name.set(selected_student[2])
            self.father_name.set(selected_student[3])
            self.phone.set(selected_student[4])




