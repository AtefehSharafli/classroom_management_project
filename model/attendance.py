class Attendance:
    def __init__(self, national_id, date, status, note=""):
#گرفتن اطلاعات اولیه حضور و غیاب (کد ملی، تاریخ، وضعیت و توضیحات)
        self.national_id = national_id
        self.date = date
        self.status = status
        self.note = note
#نمایش اطلاعات حضور و غیاب به صورت متنی
    def __repr__(self):
        return f"Attendance({self.national_id}, {self.date}, {self.status}, {self.note})"