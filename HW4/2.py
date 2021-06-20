from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self):
        self.__area =0
        self.__surronding=0

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def surronding(self):
        pass


    @staticmethod
    def draw_concat(squ_list):
        real_list=list.copy(squ_list)
        while sum(real_list) !=0:
            for i in range(len(real_list)):
                if real_list[i] ==0:
                    print(" "*squ_list[i],end="")
                else:
                    print(squ_list[i]* "*",end="")
                if real_list[i] !=0:
                    real_list[i] -=1
            print()

    @staticmethod
    def concat_area(rec_list):
        if all(isinstance(x,Rectangle) for x in rec_list):
            sum_area = 0
            for rec in rec_list:
                sum_area+=rec.area
            return sum_area

        else:
            print("All instances should be Rectangle")



class Rectangle(Shape):

    def __init__(self,length,width):
        super(Rectangle, self).__init__()
        self.length=length
        self.width = width

    @property
    def area(self):
        self.__area = self.width * self.length
        return self.__area

    @property
    def surronding(self):
        self.__surronding = 2*self.length + 2*self.width
        return self.__surronding

    def draw(self):
        print("I am drawing a Rec")

class Square(Rectangle):
    def __init__(self,length):
        super(Square, self).__init__(length=length,width=length)

rec_list=[]

rec1=Rectangle(2,3)
rec2=Rectangle(6,4)
rec3=Rectangle(5,7)
rec4=Rectangle(12,15)
rec5=Rectangle(20,30)

rec_list.append(rec1)
rec_list.append(rec2)
rec_list.append(rec3)
rec_list.append(rec4)
rec_list.append(rec5)

print(rec1.area)
print()
print(rec1.surronding)
print()
print(Shape.concat_area(rec_list))
print()
Shape.draw_concat([2,5,3])


#how to inherits properties ?
#how to work with property setter and getters in properties?
# abstract method and property don't come with each other?









