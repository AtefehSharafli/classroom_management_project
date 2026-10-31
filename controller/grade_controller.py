from business_logic.grade_bl import GradeBL
from model.grade_book import GradeBook

class GradeController:
    def __init__(self):
        self.grade_bl = GradeBL()
#ذخیره کردن نمره جدید
    def save(self,national_id, lesson_name, score):
        try:
            grad_book = GradeBook(national_id, lesson_name, score)
#اطلاعات نمره برای ذخیره شدن ارسال می شود
            self.grade_bl.save(grad_book)
            return True, "نمره با موفقیت ثبت شد."
        except Exception as e:
            return False, f"خطا در ثبت:  {e}"
#لیست نمره ها گرفته می شود
    def find_all(self):
        try:
            grades_list = self.grade_bl.find_all()
            return True, grades_list
        except Exception as e:
            return False, f"خطا در دریافت اطلاعات:{e}"