class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Создаём три объекта
rect1 = Rectangle(5, 3)  # ширина 5, высота 3
rect2 = Rectangle(4, 6)  # ширина 4, высота 6
rect3 = Rectangle(7, 8)  # ширина 7, высота 8

# Рассчитываем площадь и периметр для каждого объекта
print("Площадь прямоугольника 1:", rect1.area())
print("Периметр прямоугольника 1:", rect1.perimeter())

print("\nПлощадь прямоугольника 2:", rect2.area())
print("Периметр прямоугольника 2:", rect2.perimeter())

print("\nПлощадь прямоугольника 3:", rect3.area())
print("Периметр прямоугольника 3:", rect3.perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            raise ValueError("Деление на ноль!")

    def subtraction(self):
        return self.a - self.b


