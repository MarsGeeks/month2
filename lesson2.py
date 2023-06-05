class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius ** 2

    def info(self):
        return f'Circle radius: {self.__radius}, area:{Circle.calculate_area(self)}{Figure.unit}'

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        return f' RightTriangle side a: {self.__side_a}, side b: {self.__side_b}, area: {RightTriangle.calculate_area(self)}{Figure.unit}'

right_triangle = RightTriangle(5, 8)
print(right_triangle.calculate_area())
print(right_triangle.info())
# circle = Circle(2)
# print(circle.calculate_area())
# print(circle.info())
