class Attendance:
    def __init__(self, national_id, date, status, note=""):
        #کد ملی دانش آموز برای ارتباط با او،تاریخ جلسه،وضعیت حضور و عدم حضور و تاخیر، علت آن بررسی می شود.
        self.national_id = national_id
        self.date = date
        self.status = status
        self.note = note

    def __repr__(self):
        return f"Attendance({self.national_id}, {self.date}, {self.status}, {self.note})"