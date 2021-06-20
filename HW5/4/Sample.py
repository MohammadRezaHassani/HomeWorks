from person import Person
import UserLoggers
import logging


def sub(a, b):
    if b !=0:
        UserLoggers.sub_logger.debug("a/b=" + str(a / b))
        return a / b
    UserLoggers.sub_logger.info("Divide by zero!",exc_info=True)


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)

