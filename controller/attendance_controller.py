from business_logic.attendance_bl import AttendanceBL
from model.attendance import Attendance

class AttendanceController:
    def __init__(self):
        self.attendance_bl = AttendanceBL()

    def save(self, national_id, date, status, note):
        try:
            attendance = Attendance(national_id, date, status, note)
        #برای بررسی و ذخیره فرستادم به business_logic
            self.attendance_bl.save(attendance)
            return True, "Attendance saved successfully"
        except Exception as e:
            return False, f"save failed with {e}"

    def find_all(self):
        try:
            attendances_list = self.attendance_bl.find_all()
            return True, attendances_list
        except Exception as e:
            return False, f"Operation Failed: {e}"