import os
import pickle

class StudentDa:
    def __init__(self):
        self.filename ="data_access/data/students.dat"

    def save(self,student):
        student_list=self.find_all()
        student_list.append(student)

        os.makedirs(os.path.dirname(self.filename),exist_ok=True)
        file=open(self.filename,"wb")
        pickle.dump(student_list,file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        file=open(self.filename,"rb")
        student_list=pickle.load(file)
        file.close()
        return student_list
