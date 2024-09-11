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

Задание № 3 

class SidebarElements:

    def __init__(self, text: str, type: str, loc: str) -> str:
        self.text = text
        self.type = type = 'Кнопка'
        self.loc = loc

    def print(self):
        return print(self.type + ' - ' + self.text + ' имеет локатор ' + self.loc)

    def click(self):
        return print("Клик по кнопке - {}".format(self.text) + '\n')


text_box = SidebarElements('Text Box', type, loc='SidebarElements#text_box')
text_box.print()
text_box.click()

check_box = SidebarElements('Check Box', type, loc='SidebarElements#check_box')
check_box.print()
check_box.click()

radio_button = SidebarElements('Radio Button', type, loc='SidebarElements#radio_button')
radio_button.print()
radio_button.click()

web_tables = SidebarElements('Web Tables', type, loc='SidebarElements#web_tables')
web_tables.print()
web_tables.click()

buttons = SidebarElements('Buttons', type, loc='SidebarElements#buttons')
buttons.print()
buttons.click()

links = SidebarElements('Links', type, loc='SidebarElements#links')
links.print()
links.click()

broken_links_images = SidebarElements('Broken Links - Images', type, loc='SidebarElements#broken_links_images')
broken_links_images.print()
broken_links_images.click()

upload_and_download = SidebarElements('Upload adn Download', type, loc='SidebarElements#upload_and_download')
upload_and_download.print()
upload_and_download.click()

dynamic_properties = SidebarElements('Dynamic Properties', type, loc='SidebarElements#dynamic_properties')
dynamic_properties.print()
dynamic_properties.click()
