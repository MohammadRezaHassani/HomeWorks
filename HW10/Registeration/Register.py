from .Validations.Validators import *
from .Models import User
import json
import time
from .ProjectUtils.utils import *


class Register:

    # Get's input from user with a message and a validator
    # returns the value if the validators doesn't raise any exception
    @staticmethod
    def load_data(prompt_message, validator_func, retry=True):
        clear_Terminal()
        ret_val = None
        try:
            data = input(prompt_message)
            validator_func(data)
        except ValidationException as ve:
            print(ve.msg, end=" ")
            for i in range(3):
                time.sleep(1)
                print("!", end=" ")
            if retry:
                ret_val = Register.load_data(prompt_message, validator_func, retry)
            else:
                raise ve
        else:
            ret_val = data
            return ret_val

        return ret_val

    @classmethod
    def register_user(cls):

        user_name = cls.load_data("Enter your useName: ", name_validation)
        email = cls.load_data("Enter your Email: ", email_validation)
        phone = cls.load_data("Enter your phone:  ", phone_validation)
        password = cls.load_data("Enter Your Password: ", password_validation)
        user = User.User(phone=phone, email=email, password=password, user_name=user_name)
        clear_Terminal()
        print("cong: registration completed!!!")
        time.sleep(2)
        clear_Terminal()
        # in this step we register the user inside the users directory
        with open("/home/humanbeing/2021/Work/Maktab-Sharif/Homeworks/HW10/UserDataBase/user.json", 'w') as user_info:
            # this steps writes the user info in the corresponding file which we need
            json.dump(User.User.user_list, user_info)

    @classmethod
    def load_user_from_json_file(cls):
        file_path = cls.load_data("Enter your file_path: ", file_validation)
        json_string = ''
        with open(file_path, 'r') as json_file:
            json_string = json.load(json_file)

        user_name = json_string.get("user_name")
        email = json_string.get("email")
        password = json_string.get("password")
        phone = json_string.get("phone")
        new_user = User.User(phone=phone, email=email, password=password, user_name=user_name)
        print("cong: registration completed!!!")
        time.sleep(2)
        clear_Terminal()
        with open("/home/humanbeing/2021/Work/Maktab-Sharif/Homeworks/HW10/UserDataBase/user.json", 'w') as user_info:
            # this steps writes the user info in the corresponding file which we need
            json.dump(User.User.user_list, user_info)

    @classmethod
    def show_all_users(cls):
        # this function going to show all the users
        with open("/home/humanbeing/2021/Work/Maktab-Sharif/Homeworks/HW10/UserDataBase/user.json") as data_base:
            all_users = json.load(data_base)
        # this will gonna extract all the users and extracts them
        for i in range(len(all_users)):
            all_users[i] = User.User.extract_user_by_dict(all_users[i])
            print(all_users[i])

        time.sleep(5)
        clear_Terminal()

