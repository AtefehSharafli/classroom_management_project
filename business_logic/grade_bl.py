from data_access.grade_da import GradeDA

class GradeBL:
    def __init__(self):
        self.grade_da = GradeDA()

     #بررسی اینکه نمره معتبر باشد. بین 0تا20 یا توصیفی
    def save(self, grade_book):
        self.grade_da.save(grade_book)

    def find_all(self):
        return self.grade_da.find_all()