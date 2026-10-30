from controller.student_controller import StudentController
from controller.grade_controller import GradeController
from controller.attendance_controller import AttendanceController
from controller.lesson_controller import LessonController


print("--------------تست لایه دانش آموز---------------")
student_controller = StudentController()
success, message = student_controller.save(
    "1234567890",
    "Ali",
    "Rezaei",
    "Reza",
    "09123456789"
)
print(success,message)
print("List:", student_controller.find_all())

print("\n---------------تست لایه نمره-------------")
grade_controller = GradeController()
success, message= grade_controller.save("1234567890", "20", "math")
print(success, message)
print("List:", grade_controller.find_all())

print("\n---------------تست لایه حضور و غیاب-------------")
attendance_controller = AttendanceController()
success, message= attendance_controller.save("1234567890", "1405-08-01","حاضر","note")
print(success, message)
print("List:", attendance_controller.find_all())

print("\n-------------تست لایه درس-------------")
lesson_controller = LessonController()
success,message=lesson_controller.save("Advanced", "math")
print(success, message)
print("List:", lesson_controller.find_all())