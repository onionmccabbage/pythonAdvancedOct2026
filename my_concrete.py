# concrete classes are the ones we end up using
from my_abstract import AbstractShape

# now our Shape MUST implement the abstract features
class Shape(AbstractShape):
    # we use slots to declare the permitted name-mangled members
    __slots__ = ('__num_sides', '__colour')
    def __init__(self, sides, colour):
        self.num_sides = sides # here we call the num_sides property setter
        self.colour = colour
    @property
    def num_sides(self): # here we have a property getter method
        return self.__num_sides # we return the name-mangled property
    @num_sides.setter
    def num_sides(self, new_num_sides): # here we have a property setter method
        # we typically validate in the setter
        self.__num_sides = new_num_sides
    @property
    def colour(self):
        return self.__colour # name-mangled property
    @colour.setter
    def colour(self, new_colour):
        self.__colour = new_colour

if __name__ == '__main__':
    # we may make instances of our class
    s1 = Shape(4, 'blue')
    s1.num_sides = 4 # this calls the num_sides property setter (with validation)

