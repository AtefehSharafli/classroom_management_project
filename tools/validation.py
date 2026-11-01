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
#تبدیل به متن برای اینکه صفر های ابتدایی کد ملی حفظ شود
        national_str=str(national_id)
        if not(len(national_str)==10 and national_str.isdigit()):
            raise ValueError("Invalid National ID")