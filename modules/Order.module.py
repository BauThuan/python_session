class Circle:
    @staticmethod
    def calculate_area(radius):
        return 3.14 * radius ** 2

    def print_area(self,radius):
        area = Circle.calculate_area(radius)
        print("Diện tích của hình tròn là:", area)

circle = Circle()
circle.print_area

