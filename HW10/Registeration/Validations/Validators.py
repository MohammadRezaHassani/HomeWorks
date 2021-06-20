import re
import os


class ValidationException(Exception):
    def __init__(self, msg):
        self.msg = msg


def name_validation(name: str):
    if re.search('^([a-zA-Z](_)*){3}[A-Za-z_]*$', name):
        if len(name) > 15 or len(name) < 4:
            raise ValidationException("Invalid name Format: length  between 4 and 15 ")
        return True
    raise ValidationException("Invalid name Format")


def email_validation(email: str):
    if re.search('^[a-z0-9]+[_a-z0-9\.-]*[a-z0-9]+@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
        return True
    raise ValidationException("Invalid email Format")


def phone_validation(phone: str):
    if re.search('^09(\d{9})$|^(\+989)(\d){10}$', phone):
        return True
    raise ValidationException("Invalid name Format")


def password_validation(password: str):
    if re.search('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}', password):
        return True
    raise ValidationException("Invalid Password Format")


def file_validation(file_path: str):
    if os.path.isfile(file_path):
        return True
    raise ValidationException("Invalid File Path")
