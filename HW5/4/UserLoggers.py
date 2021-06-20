import logging

formatter1 = logging.Formatter("%(asctime)s - %(name)-10s - %(levelname)-16s -%(msecs)s - %(message)s")
formatter2 = logging.Formatter("%(asctime)s - %(levelname)-  %(message)s")

person_logger= logging.getLogger("Person")

person_logger.setLevel(logging.DEBUG)

person_f_handler = logging.FileHandler("Person.log")
person_f_handler.setLevel(logging.DEBUG)
person_f_handler.setFormatter(formatter1)

person_logger.addHandler(person_f_handler)


sub_logger = logging.getLogger("Sample11")

sub_logger.setLevel(logging.INFO)

print(sub_logger)
c_handler =logging.StreamHandler()
sample_f_handler = logging.FileHandler("Sample.log")
sample_f_handler.setLevel(logging.INFO)
c_handler.setLevel(logging.ERROR)
sample_f_handler.setFormatter(formatter1)
c_handler.setFormatter(formatter2)
sub_logger.addHandler(c_handler)
sub_logger.addHandler(sample_f_handler)







