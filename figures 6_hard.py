import math

class Figure:
    sides_count = 0

    def __init__(self, color : tuple[int, int, int], *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1 for i in range(self.sides_count)]
        self.__color = [0, 0, 0]
        if len(color) == 3 and self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = list(color)
        self.is_filled = False

    def get_color(self):
        return self.__color.copy()

    @staticmethod
    def __is_valid_color(r, g, b):
        col = (r, g, b)
        return min(col) >= 0 and max(col) <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return min(args) > 0 and len(args) == self.sides_count

    def get_sides(self):
        return self.__sides.copy()

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, len_):
        super().__init__(color, len_)
        self.__radius = len_ / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a = self._Figure__sides[0]
        b = self._Figure__sides[1]
        c = self._Figure__sides[2]
        p = (a + b + c) * 0.5
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, l):
        super().__init__(color, l, l, l, l, l, l, l, l, l, l, l, l)
        self.__side_len = max(l, 1)

    def get_volume(self):
        return self.__side_len ** 3

    
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle = Triangle((244, 21, 56), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
triangle.set_color(30, 70, 15) # Не изменится
print(triangle.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print(triangle.get_square())
print(len(triangle))
