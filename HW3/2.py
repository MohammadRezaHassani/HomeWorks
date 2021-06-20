# first exercises

import datetime


class Birthday:
    def __init__(self, year, month, day):
        self.birth_date = datetime.datetime(year, month, day)

    def year_age(self):
        today = datetime.datetime.today()
        difference_years = today.year - self.birth_date.year
        if today.month < self.birth_date.month or \
                (self.birth_date.month == today.month and today.day < self.birth_date.day):
            difference_years -= 1
        return "Age IN Year: ",difference_years

    def year_hour(self):
        today = datetime.datetime.today()
        diff = today - self.birth_date
        day, mino = diff.days, diff.seconds
        return "Age IN Hour: ",day * 24 + int(mino / 60)

    def days_to_birth(self):
        this_year_birth = datetime.datetime(datetime.datetime.today().year,
                                            self.birth_date.month,self.birth_date.day)
        today = datetime.datetime.today()
        return "Days To Birth: ",abs(today - this_year_birth).days


b1 = Birthday(1995,10,19)
print(*b1.year_age())
print(*b1.year_hour())
print(*b1.days_to_birth())

