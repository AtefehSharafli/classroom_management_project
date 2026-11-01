import re

class Validator:
#بررسی اینکه نام وارد شده معتبر باشد
    @staticmethod
    def name_validator(name):
        if not re.match(r"^[a-zA-Z]{2,30}$", name):
            raise ValueError("Invalid Name")
#بررسی اینکه نام خانوادگی وارد شده معتبر باشد
    @staticmethod
    def family_validator(family):
        if not re.match(r"^[a-zA-Z]{2,40}$", family):
            raise ValueError("Invalid Family")
# بررسی اینکه کد ملی وارد شده معتبر باشد(فقط عدد و دقیقا 10رقم باشد)
    @staticmethod
    def national_id_validator(national_id):
        if not(len(str(national_id))==10 and str(national_id).isdigit()):
            raise ValueError("Invalid National ID")