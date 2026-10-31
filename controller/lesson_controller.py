from business_logic.lesson_bl import LessonBL
from model.lesson_plan import LessonPlan

class LessonController:
    def __init__(self):
        self.lesson_bl=LessonBL()
# ذخیره کردن درس جدید
    def save(self,name, description):
        try:
            lesson_plan = LessonPlan(name,description)
#اطلاعات برای ذخیره فرستاده شود
            self.lesson_bl.save(lesson_plan)
            return (True,"درس با موفقیت ثبت شد.")
        except Exception as e:
            return False, f"خطا در ثبت: {e}"
#گرفتن لیست همه درس ها
    def find_all(self):
        try:
            lesson_list=self.lesson_bl.find_all()
            return True, lesson_list
        except Exception as e:
            return False, f"خطا در دریافت اطلاعات: {e}"