from data_access.lesson_da import LessonDa

class LessonBL:
#تابع های کار با فایل درس ها
    def __init__(self):
        self.lesson_da = LessonDa()
#ذخیره کردن درس جدید
    def save(self, lesson_plan):
#نام درس خالی نباشد
        if lesson_plan.subject!= " ":
            self.lesson_da.save(lesson_plan)
        else:
            raise ValueError("نام درس نمی تواند خالی باشد! ")
#لیست همه درس ها گرفته شود و نمایش داده شود
    def find_all(self):
        return self.lesson_da.find_all()