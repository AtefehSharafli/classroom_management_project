class LessonPlan:
#گرفتن اطلاعات اولیه درس(نام درس و توضیحات)
    def __init__(self,subject,description):
        self.subject = subject
        self._subject = subject
        self.subject_id = subject
        self.description = description