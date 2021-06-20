from itertools import takewhile
import time


def time_calculator(func):
    def inner_func(*args, **kwargs):
        start_time = time.time()
        value = func(*args)
        print("***************HailStone_series****************")
        print(value)
        end_time = time.time()
        return f"Execution_time: {end_time - start_time}"

    return inner_func


def hsg_gen(number):
    yield number
    while True:
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        yield number


@time_calculator
def hsg_info(number):
    hsg_series = list(takewhile(lambda x: x != 1, hsg_gen(number))) + [1]
    return f"hsg_series for {number} is: {*hsg_series,} \nLen: {len(hsg_series)}"


class HsgIter:
    def __init__(self, number):
        self.number = number
        self.pre_number = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 1:
            self.counter += 1
            return self.number

        if self.number == 1 and self.pre_number != 1:
            raise StopIteration

        if self.number % 2 == 0:
            self.pre_number = self.number
            self.number = self.number // 2
        else:
            self.pre_number = self.number
            self.number = 3 * self.number + 1

        return self.number


for series_num in HsgIter(7):
    print(series_num, end=" ")

print()
print(hsg_info(7))
