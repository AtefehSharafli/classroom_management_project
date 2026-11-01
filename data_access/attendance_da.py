import os
import pickle

class AttendanceDa:
    def __init__(self):
#اطلاعات حضور و غیاب در آن ذخیره شود
        self.filename="data_access/data/attendance.dat"
#ذخیره کردن لیست حضور و غیاب در فایل
    def save(self, attendance):
        attendance_list=self.find_all()
        attendance_list.append(attendance)

#اگر پوشه  data نبود.خودکار می سازد که ارور نده
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        file = open(self.filename, "wb")
        pickle.dump(attendance_list, file)
        file.close()
#خواندن و برگرداندن تمام اطلاعات از داخل فایل
    def find_all(self):
        if not os.path.exists(self.filename):
            return []

        file = open(self.filename, "rb")
        attendance_list = pickle.load(file)
        file.close()
        return attendance_list