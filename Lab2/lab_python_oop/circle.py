from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math

class Circle (Figure):

    figer_type = 'Круг'

    @classmethod
    def get_format (cls):
        return cls.figer_type


    def __init__ (self, radius_param, color_param):
        self.radius=radius_param
        self.fc= FigureColor ()
        self.fc.colorpoperty = color_param

    def square (self):
        return math.pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета, радиуса {} и площадью {}'.format(
            Circle.get_format(),
            self.fc.colorpoperty,
            self.radius,
            Circle.square(self)
        )