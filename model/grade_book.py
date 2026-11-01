class GradeBook:
#گرفتن اطلاعات اولیه نمره(کد ملی،نام درس و مقدار نمره)
    def __init__(self,national_id,lesson_name, score):
        self.national_id = national_id
        self.lesson_name = lesson_name
        self.score = score