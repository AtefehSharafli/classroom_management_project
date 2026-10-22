from business_logic.student_bl import StudentBL
from model.student import Student

class StudentController:
    def __init__(self):
        self.student_bl = StudentBL()

    def save(self,national_id,first_name,last_name, father_name, phone_number):
        try:

            student = Student(national_id,first_name,last_name,father_name,phone_number)

            self.student_bl.save(student)
            return True, "اطلاعات دانش آموز با موفقیت ثبت شد."
        except Exception as e:
            return False,f"خطا در ثبت: {e}"

    def find_all(self):
        try:

            student_list =self.student_bl.find_all()
            return True, student_list
        except Exception as e:
            return False,f" خطا در دریافت اطلاعات:{e}"
