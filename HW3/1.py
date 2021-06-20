import math


class Triangle:
    @staticmethod
    def set_coordinate(string):
        print("Enter {string} vertex X & Y : ".format(string=string), end=" ")
        return tuple(map(int, input().split()))

    @staticmethod
    def edge_calculation(f_vertex, s_vertex):
        return math.sqrt((f_vertex[0] - s_vertex[0]) ** 2 + (f_vertex[1] - s_vertex[1]) ** 2)

    def __init__(self):
        self.first_vertex = Triangle.set_coordinate("first")
        self.second_vertex = Triangle.set_coordinate("second")
        self.third_vertex = Triangle.set_coordinate("third")
        self.first_edge = round(Triangle.edge_calculation(self.first_vertex, self.second_vertex), 3)
        self.second_edge = round(Triangle.edge_calculation(self.second_vertex, self.third_vertex), 3)
        self.third_edge = round(Triangle.edge_calculation(self.first_vertex, self.third_vertex), 3)
        self.env = round(self.first_edge + self.second_edge + self.third_edge, 3)

    def surface_calculation(self):
        x = self.first_vertex[0] * (self.second_vertex[1] - self.third_vertex[1])
        y = self.second_vertex[0] * (self.third_vertex[1] - self.first_vertex[1])
        z = self.third_vertex[0] * (self.first_vertex[1] - self.second_vertex[1])
        return "Triangle Surface : {surface}".format(surface=abs(x + y + z)/2)

    def triangle_edges(self):
        return "Triangle edges length: ({}, {}, {})".format(self.first_edge, self.second_edge, self.third_edge)

    def environment_calculation(self):
        return "Triangle env: {} ".format(self.env)

    def center_calculation(self):
        return ["Triangle centroid : ",
                (round((self.first_vertex[0] + self.second_vertex[0] + self.third_vertex[0]) / 3, 3),
                 round((self.first_vertex[1] + self.second_vertex[1] + self.third_vertex[1]) / 3, 3))]

    def type_calculation(self):
        if self.first_edge == self.second_edge or \
                self.second_edge == self.third_edge or \
                self.first_edge == self.third_edge:
            return "Type: Equivalent of the legs"
        elif self.first_edge == self.second_edge and \
                self.second_edge == self.third_edge:
            return "Type: Equilateral"

        elif self.first_edge ** 2 + self.third_edge ** 2 == self.second_edge ** 2 or \
                self.first_edge ** 2 + self.second_edge ** 2 == self.third_edge ** 2 or \
                self.second_edge ** 2 + self.third_edge ** 2 == self.first_edge ** 2:
            return "Type: Qaem Al-Zawiya"
        else:
            return "Type: Normal"

    def info(self):
        print()
        print("The Object information: ")
        print(t1.surface_calculation())
        print(t1.type_calculation())
        print(*t1.center_calculation())
        print(t1.triangle_edges())
        print(t1.environment_calculation())


t1 = Triangle()
t1.info()
