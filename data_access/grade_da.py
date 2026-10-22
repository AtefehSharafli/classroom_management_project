class GradeDA:
    def __init__(self):
        self.grades_list = []

    def save(self,grade_book):
        self.grades_list.append(grade_book)
        return True

    def find_all(self):
        return self.grades_list