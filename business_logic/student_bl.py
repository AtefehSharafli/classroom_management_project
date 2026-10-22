from data_access.student_da import StudentDa

class StudentBL:
    def __init__(self):
        self.student_da = StudentDa()

    def save(self, student):
        self.student_da.save(student)

    def find_all(self):
        return self.student_da.find_all()