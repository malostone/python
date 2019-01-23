import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle():
    def __init__(self,x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        
    def get_square(self):
        self.square = round(0.5 * ((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3)))
        return print("Площадь треугольника: ", self.square)
    
    def get_perimeter(self):
        self.ab = math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2))
        self.ac = math.sqrt(((self.x3-self.x1)**2)+((self.y3-self.y1)**2))
        self.bc = math.sqrt(((self.x3-self.x2)**2)+((self.y3-self.y2)**2))
        self.perimetr =round(self.ab + self.ac + self.bc)
        return print("Периметр треугольника: ", self.perimetr)

    def get_hight(self):
        self.hight = round((2*self.square)/self.ab)
        return print("Высота треугольника: ",self.hight)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


triangle1 = Triangle(2,-3,1,1,-6,5)        
triangle1.get_square()
triangle1.get_perimeter()
triangle1.get_hight()

class Trapeze():
    def __init__(self,x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def get_side(self):
        self.a = round(math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2)))
        self.b = round(math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2)))
        self.c = round(math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)))
        self.d = round(math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2)))
        return print("Длина сторон: ", "AB: " , self.a, ", BC: ", self.c, ", CD: ", self.d, ", DC: ", self.b)

        
    def get_perimeter(self):
        self.perimeter =round(self.a + self.b + self.c + self.d)
        return print("Периметр трапеции: ", self.perimeter)
    
    def get_square(self):
        self.square =round(((self.a + self.b) / 2)*(math.sqrt((self.c ** 2)-((((self.b - self.a) **2 ) +(self.c ** 2)-(self.d ** 2))/(2 * (self.b - self.a))))))
        return print("Площадь трапеции: ", self.square)

    def is_trapeze(self):
        if self.c == self.d:
            print("Трапеция равнобедренная")
        else:
            print("Трапеция неравнобедренная")

trapeze1 = Trapeze(2,4,0,2,0,7,2,5)        
trapeze1.get_side()
trapeze1.get_square()
trapeze1.get_perimeter()
trapeze1.is_trapeze()

trapeze2 = Trapeze(4,10,3,4,-8,-9,7,15)        
trapeze2.get_side()
trapeze2.get_square()
trapeze2.get_perimeter()
trapeze2.is_trapeze()
 
