# classes in python are used to create instances attributes can be set either in the body of the class or outside the body
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f"move to {self.x}, {self.y}")

    def rotate(self):
        print('rotate')


point = Point(12, 3)
point.move()
print(point.x)
