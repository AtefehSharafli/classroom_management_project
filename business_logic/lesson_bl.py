from data_access.lesson_da import LessonDa

class LessonBL:
    def __init__(self):
        self.lesson_da = LessonDa()

    def save(self, lesson_plan):
        if lesson_plan.subject!= " ":
            self.lesson_da.save(lesson_plan)
        else:
            raise ValueError("نام درس نمی تواند خالی باشد! ")

    def find_all(self):
        return self.lesson_da.find_all()