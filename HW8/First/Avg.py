import sys


def average_calculator():
    try:
        grades = list(map(float, sys.argv[1:]))
        return f"Grades Average:{sum(grades) / len(grades):>4}"
    except ValueError:
        return "Error: Expected digits"


print(average_calculator())
