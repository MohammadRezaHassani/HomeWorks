from NumberTable import first_digit as f_dig, Second_digit as S_dig, Exceptions as Ex, great_digits as g_dig
import os


class PrimException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Helper:

    @staticmethod
    def str_num_format(num):
        base_power = 3
        dig_counter = -1
        ans_str = ""
        while num > 0:
            temp_num = num % (10 ** base_power)
            num = num // (10 ** base_power)
            dig_counter += 1
            ans_str = Helper.converter(dig_counter, temp_num) + " " + ans_str

        return ans_str

    @staticmethod
    def converter(dig_counter, temp_num):
        ans_str = ""
        temp_num = str(temp_num)
        if len(temp_num) < 3:
            added = 3 - len(temp_num)
            temp_num = "0" * added + temp_num

        first_digit = int(temp_num[2])
        second_digit = int(temp_num[1])
        third_digit = int(temp_num[0])

        if second_digit == 1:
            ans_str = Ex[first_digit] + ans_str
        else:
            ans_str = S_dig[second_digit] + " " + f_dig[first_digit] + " " + ans_str

        if third_digit > 0:
            ans_str = f_dig[third_digit] + "  hundred" + " " + ans_str

        ans_str += " " + g_dig[dig_counter]

        return ans_str


class MulPrimal:
    class Decorators:
        @classmethod
        def string_p(cls, func):
            def inner_func(self, *args, **kwargs):
                value = func(self)
                return Helper.str_num_format(value)

            return inner_func

        @classmethod
        def reminder(cls, number):
            def inner_1(func):
                def inner_2(self, *args, **kwargs):
                    value = func(self)
                    while True:
                        try:
                            if value == 0:
                                return
                            number = int(input("Enter your division number: "))
                            return Helper.str_num_format(value % number)
                        except ValueError:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Error: Integer required")

                return inner_2

            return inner_1

    @staticmethod
    def check_primal(num):
        for i in range(2, num):
            if not isinstance(i, int):
                return False
            if num % i == 0:
                return False
        return True

    @staticmethod
    def mul_array(array):
        ans = 1
        for num in array:
            ans *= num
        return ans

    def mul_primal(self):
        try:
            self.check_num_list()
            return MulPrimal.mul_array(self.num_list)
        except PrimException as Pex:
            print(Pex.msg)
            return 0

    def __init__(self, num_list):
        self.num_list = num_list

    @Decorators.string_p
    def mul_primal_str(self):
        return self.mul_primal()

    @Decorators.reminder(number=None)
    def mul_primal_remind(self):
        return self.mul_primal()

    def check_num_list(self):
        for i in self.num_list:
            if not MulPrimal.check_primal(i):
                raise PrimException("Error :: Enter Prime Numbers")


m1 = MulPrimal([3, 11])

print(m1.mul_primal_str())
print(m1.mul_primal_remind())
