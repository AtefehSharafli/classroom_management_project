class LessonDa:
    def __init__(self):
        self.lesson_list=[]

    def save(self,lesson_plan):
        self.lesson_list.append(lesson_plan)
        return True

    def find_all(self):
        return self.lesson_list