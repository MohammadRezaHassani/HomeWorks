class Book:

    def __init__(self,name,book_num,price):
        self.name = name
        self.book_num =book_num
        self.price = price
        self.__class__.inc_book_num()

    def __str__(self):
        return f"---book info-- \n book-name: {self.name} \n " \
               f"book-price: {self.price} \n book-num: {self.book_num} "

    @classmethod

    def initilize_class_attr(cls):
        cls.total_book_num =0

    @classmethod

    def inc_book_num(cls):
        cls.total_book_num +=1

    @classmethod
    def dec_book_num(cls):
        cls.total_book_num -= 1

Book.initilize_class_attr() #in order to initilize the class atrs

b1=Book("Golestan",1,1000)
print(b1)
