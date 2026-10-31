from data_access.student_da import StudentDa

class StudentBL:
#تابع های بخش دانش آموزان
    def __init__(self):
        self.student_da = StudentDa()
#ذخیره کردن دانش آموز حدید
    def save(self, student):
        return self.student_da.save(student)
#لیست همه دانش آموزان گرفته شود و نمایش آن
    def find_all(self):
        return self.student_da.find_all()