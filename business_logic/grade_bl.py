from data_access.grade_da import GradeDA

class GradeBL:
#ساخت تابع های کار با فایل نمره ها
    def __init__(self):
        self.grade_da = GradeDA()

     #نمره جدید ذخیره شود بین 0تا20 یا توصیفی
    def save(self, grade_book):
        self.grade_da.save(grade_book)
#همه نمره ها گرفته شود و نشان داده شود
    def find_all(self):
        return self.grade_da.find_all()