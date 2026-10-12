# concrete classes are the ones we end up using
from my_abstract import AbstractShape

# now our Shape MUST implement the abstract features
class Shape(AbstractShape):
    # we use slots to declare the permitted name-mangled members
    __slots__ = ('__num_sides', '__colour')
    '''This class implements the abstract shape class with colour and num_sides'''
    def __init__(self, sides=4, colour='blue'): # we may choose to set defaults here
        self.num_sides = sides # here we call the num_sides property setter
        self.colour = colour
    @property
    def num_sides(self): # here we have a property getter method
        return self.__num_sides # we return the name-mangled property
    @num_sides.setter
    def num_sides(self, new_num_sides): # here we have a property setter method
        # we typically validate in the setter
        if type(new_num_sides) in (int,) and new_num_sides>0: # here is a one-member tuple
            self.__num_sides = new_num_sides
        else:
            raise TypeError('Number of sides must be a positive integer')
    @property
    def colour(self):
        return self.__colour # name-mangled property
    @colour.setter
    def colour(self, new_colour):
        '''Colour should be a non-empty string'''
        if type(new_colour) == str and new_colour != '':
            self.__colour = new_colour
        else:
            self.__colour = 'blue' # we choose to set a sensible default

if __name__ == '__main__':
    # we may make instances of our class
    s1 = Shape(4, 'blue')
    s2 = Shape() # a blue 4-sided shape
    s3 = Shape(6) # default to blue
    # s1.num_sides = '4' # this calls the num_sides property setter (with validation)
    print(s3, s3.colour, s3.num_sides) # here we call the getter methods

