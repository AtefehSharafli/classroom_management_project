import re

class Validator:
    @staticmethod
    def name_validator(name):
        if not re.match(r"^[a-zA-Z]{2,30}$", name):
            raise ValueError("Invalid Name")

    @staticmethod
    def family_validator(family):
        if not re.match(r"^[a-zA-Z]{2,40}$", family):
            raise ValueError("Invalid Family")

    @staticmethod
    def national_id_validator(national_id):
        if not(len(str(national_id))==10 and str(national_id).isdigit()):
            raise ValueError("Invalid National ID")