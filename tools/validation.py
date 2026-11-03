import re

class Validator:
#بررسی اینکه نام وارد شده معتبر باشد
    @staticmethod
    def name_validator(name):
        pattern=r"^[\u0600-\u06FFa-zA-Z\s]+$"
#        if not re.match(r"^[\u0600-\u06FFa-zA-Z\s\u200c]{2,30}$", name):
        if not re.match(pattern,name):
            raise ValueError("Invalid Name")
#بررسی اینکه نام خانوادگی وارد شده معتبر باشد
    @staticmethod
    def family_validator(family):
        pattern=r"^[\u0600-\u06FFa-zA-Z\s]+$"
        if not re.match(pattern,family):
 #       if not re.match(r"^[\u0600-\u06FFa-zA-Z\s\u200c]{2,40}$", family):
            raise ValueError("Invalid Family")
# بررسی اینکه کد ملی وارد شده معتبر باشد(فقط عدد و دقیقا 10رقم باشد)
    @staticmethod
    def national_id_validator(national_id):
        validation=str(national_id).strip()
#بررسی اینکه کدملی دقبقا 10 رقم باشد وفقط عدد باشد و صفرها هم حفظ شوند
        if not (len(validation)==10 and validation.isdigit()):
            raise ValueError("Invalid National ID")
