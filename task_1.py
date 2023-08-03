class TriangleError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TriangleSideError(TriangleError):
    def __init__(self, side):
        self.side = side
        message = f"Длина стороны треугольника не может быть отрицательной или нулевой: {side}"
        super().__init__(message)


class TriangleNotExistError(TriangleError):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        message = f"Треугольник со сторонами {a}, {b}, и {c} не существует."
        super().__init__(message)


class TriangleChecker:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise TriangleSideError(min(a, b, c))

        self.a = a
        self.b = b
        self.c = c

    def exists_triangle(self):
        return self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b

    def get_triangle_type(self):
        if not self.exists_triangle():
            raise TriangleNotExistError(self.a, self.b, self.c)

        if self.a == self.b == self.c:
            return "Равносторонний треугольник."
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "Равнобедренный треугольник."
        else:
            return "Разносторонний треугольник."


try:
    triangle1 = TriangleChecker(3, 4, 5)
    print(triangle1.exists_triangle())
    print(triangle1.get_triangle_type())  # Вывод: Разносторонний треугольник

    triangle2 = TriangleChecker(5, 5, 5)
    print(triangle2.exists_triangle())
    print(triangle2.get_triangle_type())  # Вывод: Равносторонний треугольник

    triangle3 = TriangleChecker(2, 3, 10)
    print(triangle3.exists_triangle())
    print(triangle3.get_triangle_type())
except TriangleError as e:
    print(f"Ошибка: {e}")
