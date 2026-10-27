from controller.student_controller import StudentController
from model.student import Student

from controller.lesson_controller import LessonController
from model.lesson_plan import LessonPlan

from controller.grade_controller import GradeController
from model.grade_book import GradeBook

from controller.attendance_controller import AttendanceController
from model.attendance import Attendance

print("--------------تست لایه دانش آموز---------------")
student_controller = StudentController()
success, message = student_controller.save(
    "1234567890",
    "Ali",
    "Rezaei",
    "Mohammad",
    "12345678"
)
print(success,message)
print("List:", student_controller.find_all())

print("\n-------------تست لایه درس-------------")
lesson_controller = LessonController()
success,message=lesson_controller.save("101", "math")
print(success, message)
print("List:", lesson_controller.find_all())

print("\n---------------تست لایه نمره-------------")
#grade_controller = GradeController()
#success, message= grade_controller.save("1234567890", "20", "ریاضی")
#print(success, message)
#print("List:", grade_controller.find_all())

print("\n--------------تست لایه حضور و غیاب----------------")
#attendance_controller = AttendanceController()
#success, message=attendance_controller()
#print(success, message)
#print("List:", attendance_controller.find_all())