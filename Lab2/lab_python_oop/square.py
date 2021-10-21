from lab_python_oop.rectangle import Rectangle


class Square (Rectangle):

    figer_type = 'Квадат'

    @classmethod
    def get_format (cls):
        return cls.figer_type


    def __init__ (self, side_param, color_param):
        self.side=side_param
        super().__init__(self.side,self.side,color_param)

    def __repr__(self):
        return '{} {} цвета, со стороной {} и площадью {}'.format(
            Square.get_format(),
            self.fc.colorpoperty,
            self.side,
            Rectangle.square(self )
        )