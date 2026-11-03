from tools.validation import  Validator

class Student:
#گرفتن اطلاعات اولیه دانش آموز (کد ملی،نام،نام خانوادگی، نام پدر و شماره تماس)
    def __init__(self,first_name,last_name,national_id,father_name,phone_number):
        self._first_name = first_name
        self._last_name = last_name
        self._national_id = national_id
        self.father_name = father_name
        self.phone_number = phone_number

#گرفتن و بررسی درست بودن نام
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        Validator.name_validator(value)
        self._first_name = value

#گرفتن و بررسی درست بودن نام خانوادگی
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        Validator.family_validator(value)
        self._last_name = value

# گرفتن و بررسی صحت کد ملی
    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, value):
        Validator.national_id_validator(value)
        self._national_id = value

#نمایش اطلاعات دانش آموز به صورت متن
    def __repr__(self):
        return f"Student({self.first_name}, {self.last_name},{self.national_id},  {self.father_name}, {self.phone_number})"

    def to_tuple(self):
        return (self.first_name, self.last_name,self.national_id,self.father_name, self.phone_number)

