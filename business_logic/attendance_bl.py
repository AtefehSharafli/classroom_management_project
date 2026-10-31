from data_access.attendance_da import AttendanceDa

class AttendanceBL:
#ارتباط با فایل ذخیره اطلاعات
    def __init__(self):
        self.attendance_da = AttendanceDa()
# حضور و غیاب دانش آموزان ذخیره شود
    def save(self, attendance):
        if attendance.status in["تاخیر" , "غایب"  , "حاضر"]:
            self.attendance_da.save(attendance)
        else:
            raise ValueError("وضعیت حضور و غیاب نامعتبر است ! ")
#تمام حضور و غایب های ذخیره شده نشان داده شود
    def find_all(self):
        return self.attendance_da.find_all()
