class GradeDA:
    def __init__(self):
#لیست خالی برای نگهداری نمره ها
        self.grades_list = []
#به لیست نمره جدید اضافه شود
    def save(self,grade_book):
        self.grades_list.append(grade_book)
        return True
#برگرداندن تمام نمره های ذخیره شده
    def find_all(self):
        return self.grades_list