
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): return
    @abstractmethod
    def perimeter(self): return

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False
    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False
    def __sub__(self, other):
        return self.perimeter() - other.perimeter()
    def __mul__(self, other):
        return self.perimeter() * 1

#-----------------------------------------
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            self._radius = 1
        else:
            self._radius = radius
    def __getitem__(self):
        return self._radius
    def __setitem__(self, r):
        self._radius = r
    def area(self):
        return float(math.pi * (self._radius**2))
    def perimeter(self):
        return float(2 * math.pi * self._radius)
    def __str__(self):
        return "Circle: radius = [" + str(self._radius) + "]"
#--------------------------------------------------
class Rectangle(Shape):
    def __init__(self, width, height):
        if width < 0:
            self._width = 1
        else:
            self._width = width
        if height < 0:
            self._height = 1
        else:
            self._height = height

    def getWidth(self):
        return float(self._width)
    def setWidth(self, width):
        self._width = width
    def getHeight(self):
         return float(self._height)
    def setHeight(self, height):
        self._height = height
    def area(self):
        return float(self._width * self._height)
    def perimeter(self):
        return float(2 * self._width + 2 * self._height)

    def __str__(self):
        return "Rectangle: width = [" + str(self._width) + "], height = [" + str(self._height) + "]"
#-------------------------------------
class Square(Rectangle):
    def __init__(self, length):
        self._width = length
        self._height = length
    def __str__(self):
        return "Square: length = [" + str(self._width) + "]"
#----------------------------------------
class ShapesCollection(ABC):
    def __init__(self):
        self.__shapes = []
    def __getitem__(self, i):
        return self.__shapes[i]
    def __setitem__(self, i, shape):
        self.__shapes[i] = shape
    def __len__(self):
        return len(self.__shapes)

    def insert(self, shape):
        if not self.__shapes:
            self.__shapes.append(shape)
        for i in range(len(self.__shapes)):
            if self.__shapes[i] > shape:
                break
        self.__shapes = self.__shapes[:i] + [shape] + self.__shapes[i:]

    def biggestPerimeterDiff(self):
        max_diff = max([self.__shapes[i+1] - self.__shapes[i] for i in range(len(self.__shapes) - 1) if self.__shapes[i] * self.__shapes[i+1]])
        return max_diff

    def sameAreaAs(self, s):
        lst = []
        for i in range(len(self.__shapes)):
            if self.__shapes[i] == s:
                lst.append(s.__str__())
        return lst

    def howManyQuadrilaterals(self):
        counter = 0
        for i in range(len(self.__shapes)):
            if type(self.__shapes[i]) == Rectangle or type(self.__shapes[i]) == Square:
                counter += 1
        return counter
    def __str__(self):
        self.__shapes.insert(0, "Collection in Shapes:")
        return str(self.__shapes)
#----------------------------------------------

C = Circle(3)
print(C)
print(C.area())
print(C.perimeter())

R = Rectangle(5, 10)
print(R)
print(R.area())
print(R.perimeter())

S = Square(7)
print(S)
print(S.area())
print(S.perimeter())

C2 = Circle(37)
print(C)
print(C2.area())
print(C2.perimeter(), '\n')

SC = ShapesCollection()
SC.insert(R)
SC.insert(C2)
SC.insert(Rectangle(4, 9))
SC.insert(S)
SC.insert(C)

print('\n'.join(map(str, SC)))
print('\n')
print("Same area as s:", SC.sameAreaAs(S))
print("num of Quadrilaterals: ", SC.howManyQuadrilaterals())
print("max diff perimetters:", SC.biggestPerimeterDiff())
