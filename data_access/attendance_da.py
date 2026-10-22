import os
import pickle

class AttendanceDa:
    def __init__(self):
#فایلی که اطلاعات در آن ذخیره شده
        self.filename="data_access/data/attendance.dat"
#اطلاعات قبلی خوانده می شود و اطلاعات جدید اضافه می  شود
    def save(self, attendance):
        attendance_list=self.find_all()
        attendance_list.append(attendance)

#اگر پوشه  data نبود.خودکار می سازد که ارور نده
        so.makedirs(os.path.dirname(self.filename), exist_ok=True)
        file = open(self.filename, "wb")
        pickle.dump(attendance_list, file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []

        file = open(self.filename, "rb")
        attendance_list = pickle.load(file)
        file.close()
        return attendance_list