# Any class may inherit
from my_concrete import Shape

# unless we say otherwise, every class inherits from 'object'
class Figure(Shape):
    '''Figure inheirsts from Shape but adds a name property'''
    def __init__(self, sides=4, colour='blue', name='default'):
        super().__init__(sides, colour) # this calls the __init__ of the parent class
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and len(new_name) >0:
            self.__name = new_name
        else:
            self.__name == 'default'

if __name__ =='__main__':
    f1 = Figure(7, 'coffee', 'septagon') # a blue figure with 6 sides

    print(f1.colour, f1.name)


