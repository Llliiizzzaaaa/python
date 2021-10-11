from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_format(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width_param, height_param, color_param):
        self.width = width_param
        self.height = height_param
        self.fc = FigureColor()
        self.fc.colorpoperty = color_param

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета, шириной {}, высотой {} и площадью {}'.format(
            Rectangle.get_format(),
            self.fc.colorpoperty,
            self.width,
            self.height,
            Rectangle.square(self)
        )
