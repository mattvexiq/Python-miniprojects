class Car:
    def __init__(self, size, color, brand):
        self.size = size
        self.color = color
        self.brand = brand

    def paint_blue(self):
        self.color = "blue"

    def say_color(self):
        print(self.color)

    def say_size(self):
        print(self.size)

    def say_brand(self):
        print(self.brand)

    def vroom(self):
        print("vroom")


car1 = Car("big", "red", "tesla")
car1.vroom()
car1.say_color()
car1.paint_blue()
car1.say_color()
car2 = Car("small", "purple", "ford")
car2.vroom()
car2.say_color()
car2.paint_blue()
car2.say_color()
