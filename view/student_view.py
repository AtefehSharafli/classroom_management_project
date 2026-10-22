from tkinter import *
from tkinter import ttk, messagebox
from controller.student_controller import StudentController

class StudentView:
    def __init__(self):
        self.controller = StudentController()

        self.win=Tk()
        self.win.geometry("820x400")
        self.win.title("مدیریت دانش آموزان")

        Label(self.win, text="نام").place(x=63, y=20)
        self.first_name = StringVar()
        Entry(self.win, textvariable=self.first_name, width=22).place(x=110, y=20)

        Label(self.win, text="نام خانوادگی").place(x=20, y=70)
        self.last_name = StringVar()
        Entry(self.win, textvariable=self.last_name,width=22).place(x=110, y=70)

        Label(self.win, text="کد ملی").place(x=48, y=120)
        self.national_id = StringVar()
        Entry(self.win, textvariable=self.national_id,width=22).place(x=110, y=120)

        Label(self.win, text="نام پدر").place(x=48, y=170)
        self.father_name=StringVar()
        Entry(self.win, textvariable=self.father_name,width=22).place(x=110, y=170)

        Label(self.win, text="شماره تماس").place(x=20, y=220)
        self.phone = StringVar()
        Entry(self.win, textvariable=self.phone, width=22).place(x=110, y=220)

        Button(self.win,text="ذخیره", command=self.save_click, width=18).place(x=110, y=275)

        self.table= ttk.Treeview(self.win, show="headings", columns=[1,2,3,4,5])
        self.table.place(x=280, y=20, height=350, width=510)

        self.table.column(1, width=90)  #نام
        self.table.column(2, width=110)   #نام خانوادگی
        self.table.column(3, width=100)  #کد ملی
        self.table.column(4, width=90)   #نام پدر
        self.table.column(5, width=110)  #شماره تماس


        self.table.heading(1, text="نام")
        self.table.heading(2, text="نام خانوادگی")
        self.table.heading(3, text="کد ملی")
        self.table.heading(4, text="نام پدر")
        self.table.heading(5, text="تلفن")

        self.table.bind("<ButtonRelease>", self.table_click )

        self.reset_from()
        self.win.mainloop()

    def reset_from(self):
        self.first_name.set("")
        self.last_name.set("")
        self.national_id.set("")
        self.father_name.set("")
        self.phone.set("")

        for item in self.table.get_children():
            self.table.delete(item)

        status, result= self.controller.find_all()
        if status:
            for student in result:
                self.table.insert("", END , values=student. to_tuple())

    def save_click(self):
        status, message=self.controller.save(
            self.first_name.get(),
            self.last_name.get(),
            self.national_id.get(),
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
            self.first_name.set(selected_student[0])
            self.last_name.set(selected_student[1])
            self.national_id.set(selected_student[2])
            self.father_name.set(selected_student[3])
            self.phone.set(selected_student[4])




