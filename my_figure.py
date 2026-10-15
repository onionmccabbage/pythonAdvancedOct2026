# Any class may inherit
from my_concrete import Shape

# unless we say otherwise, every class inherits from 'object'
class Figure(Shape):
    '''Figure inherits from Shape but adds a name property'''
    # we may need to creae properties of the class (not of specific instances)
    num_instances = 0 # here this property belongs to this class

    def __init__(self, sides=4, colour='blue', name='default'):
        super().__init__(sides, colour) # this calls the __init__ of the parent class
        # Shape.__init__(sides, colour) # also works
        self.__name = name
        # each time we create an instance, we will increment the num_instances
        Figure.num_instances += 1
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and len(new_name) >0:
            self.__name = new_name
        else:
            self.__name == 'default'
    # we can declare class methods (functions which belong to the class, rather than specific instances)
    def count(): # NB we do not use 'self' for class methods
        return f'There are {Figure.num_instances} instanes'

if __name__ =='__main__':
    f1 = Figure(7, 'coffee', 'septagon') # a blue figure with 6 sides
    f2 = Figure(12, 'green', 'twelve-sided')
    print(f1.colour, f1.name)
    # we may access class properties like this
    print(Figure.num_instances)
    # print will inherit from Shape
    print(f2)



