
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        ''' If the width or height is larger than 50 return "Too big for picture" '''
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        string = (('*' * self.width) + '\n') * self.height
        return string

    def get_amount_inside(self, shape):
        ''' Returns the number of times the shape passed in could fit in the main shape '''
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return f"Square(side={self.height})"

    def set_side(self, side):
        self.width = side
        self.height = side


r = Rectangle(8, 4)
s = Square(5)
print(s)