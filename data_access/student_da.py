import os
import pickle

class StudentDa:
    def __init__(self):
        self.filename ="data_access/data/students.dat"

    def save(self,student):
        student_list=self.find_all()
        student_list.append(student)

        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename,"wb") as file:
         pickle.dump(student_list,file)


    def find_all(self):
        if not os.path.exists(self.filename)or os.path.getsize(self.filename) == 0:
            return []
        try:
            with open(self.filename,"rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            return []

