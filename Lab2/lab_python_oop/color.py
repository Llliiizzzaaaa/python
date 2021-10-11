
class FigureColor:

    def __init__(self):
        self.color = None

    @property
    def colorproperty (self):

        return self.color

    @colorproperty.setter
    def colorpoperty (self, value):

        self.color = value
