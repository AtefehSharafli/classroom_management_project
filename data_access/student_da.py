import os
import pickle

class StudentDa:
    def __init__(self):
#آدرس فایلی که اطلاعات دانش آموزان در آن ذخیره می شود
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(current_dir, "students.dat")
#ذخیره کردن دانش آموز جدید در فایل
    def save(self,student):
        student_list=self.find_all()
        student_list.append(student)
#اگر پوشه وجود نداشت خودکار بسازه
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename,"wb") as file:
         pickle.dump(student_list,file)

#خواندن و برگرداندن لیست دانش آموزان از فایل
    def find_all(self):
        if not os.path.exists(self.filename)or os.path.getsize(self.filename) == 0:
            return []
        try:
            with open(self.filename,"rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            return []

