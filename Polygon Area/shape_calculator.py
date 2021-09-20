class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        return (('*' * self.width + '\n') * self.height)

    def get_amount_inside(self, rect):
        return (self.width // rect.width) * (self.height // rect.height)


class Square(Rectangle):
    
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def __repr__(self):
        return 'Square(side={})'.format(self.width)

    def set_side(self, side_length):
        self.width =  side_length
        self.height = side_length
    
    def set_width(self, side_length):
        self.set_side(side_length)
        self.set_side(side_length)


