class LessonDa:
    def __init__(self):
#لیست خالی برای ذخیره کردن درس ها
        self.lesson_list=[]
#اضافه کردن درس جدید به لیست
    def save(self,lesson_plan):
        self.lesson_list.append(lesson_plan)
        return True
#لیست تمام درس ها برگردانده شود
    def find_all(self):
        return self.lesson_list