from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rectangle = Rectangle(20, 21, "синего")
    circle = Circle(20, "зеленого")
    square = Square(20, "красного")
    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()
