from tools.validation import  Validator

class Student:
#گرفتن اطلاعات اولیه دانش آموز (کد ملی،نام،نام خانوادگی، نام پدر و شماره تماس)
    def __init__(self,national_id, first_name,last_name,father_name,phone_number):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.phone_number = phone_number

#گرفتن و بررسی صحت کد ملی
    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, value):
        Validator.national_id_validator(value)
        self._national_id = value
#گرفتن و بررسی درست بودن نام
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        Validator.name_validator(value)
        self.__first_name = value
#گرفتن و بررسی درست بودن نام خانوادگی
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        Validator.family_validator(value)
        self.__last_name = value
#نمایش اطلاعات دانش آموز به صورت متن
    def __repr__(self):
        return f"Student({self.national_id}, {self.__first_name}, {self.__last_name}, {self.father_name}, {self.phone_number})"

    def to_tuple(self):
        return (self.national_id, self.first_name, self.last_name, self.father_name, self.phone_number)

