import datetime
import os
import logging


# "%Y-%M-%D %H:%M:%S"


class Operations:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


class DateObject:
    def __init__(self, date_format):
        self._date = None
        self.date_format = date_format

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, my_date):
        counter = 0
        while True:
            Operations.clear()
            try:
                self._date = datetime.datetime.strptime(my_date, self.date_format)
            except(ValueError, TypeError):
                logging.info(f"Error: Wrong input Format")
                my_date = input(f"Enter date with format {counter} {self.date_format}: ")
            else:
                break
            counter +=1

    @staticmethod
    def format_input(msg):
        return input(f"Enter format for your{msg} Date like '%Y-%m-%d %H:%M:%S' :  ")

    @staticmethod
    def date_input(format):
        return input(f"Enter Date with format {format}: ")


class DateArithmetic:
    obj_date: DateObject  # object Attribute
    std_start_date: DateObject  # class Attribute
    std_end_date: DateObject  # class Attribute
    std_start_date = None
    std_end_date = None

    def __sub__(self, other):
        return (self.obj_date.date - other.obj_date.date).total_seconds()

    def __init__(self, date_format, date):
        self.obj_date = DateObject(date_format)
        self.obj_date.date = date

    @classmethod
    def init_class_attrs(cls):
        date_format = DateObject.format_input("daylight saving days")
        cls.std_start_date = DateObject(date_format)
        cls.std_start_date.date = DateObject.date_input(date_format)
        cls.std_end_date = DateObject(date_format)
        cls.std_end_date.date = DateObject.date_input(date_format)

    def dst_nums(self, end_date):
        dst_num = 0
        dst_num += self.year_dst_date_with_start_point() + end_date.year_dst_date_with_start_point()
        for year in range(self.obj_date.date.year + 1, end_date.obj_date.date.year):
            dst_num += 2

        return dst_num

    def leap_years_num(self, end_date):
        leap_year_num = 0
        for year in range(self.obj_date.date.year + 1, end_date.obj_date.date.year + 1):
            if DateArithmetic.check_year_leap(year):
                leap_year_num += 1

            return leap_year_num

    def year_dst_date_with_start_point(self):
        if self.obj_date.date.month <= self.__class__.std_start_date.date.month and \
                self.obj_date.date.day <= self.__class__.std_start_date.date.day and \
                self.obj_date.date.hour <= self.__class__.std_start_date.date.hour:
            return 2

        elif self.obj_date.date.month <= self.__class__.std_end_date.date.month and \
                self.obj_date.date.day <= self.__class__.std_end_date.date.day and \
                self.obj_date.date.hour <= self.__class__.std_end_date.date.hour:
            return 1

        return 0

    @staticmethod
    def check_year_leap(year: int):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


if __name__ == '__main__':
    DateArithmetic.init_class_attrs()
    da1 = DateArithmetic("%Y-%m-%d %H:%M:%S", "1400-2-23 01:00:00")
    da2 = DateArithmetic("%Y-%m-%d %H:%M:%S", "1400-2-23 00:00:00")
    print(da1 - da2)
    print(da1.leap_years_num(da2))
    print(da1.dst_nums(da2))



