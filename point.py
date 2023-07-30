class Point:
    default_color = "red"

    def draw(self):
        print(f"point({self.x},{self.y})")

    def __init__(self, x, y):
        self.x = x
        self.y = y


abc = Point(1, 2)
abc.z = 1
print(type(abc))
print(isinstance(abc, int))
abc.draw()
Point.default_color = "YELLOW"
another = Point(3, 4)
print(another.default_color)
another.draw()
