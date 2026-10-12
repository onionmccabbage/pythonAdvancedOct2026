# we may create abstract classes
# both list and tuple are ordinal collections
# they both use abstract notions
from abc import ABCMeta, abstractmethod


# We decide on features our concrete classes will need
class AbstractShape(metaclass=ABCMeta):
    __slots__ = ('__num_sides', '__colour')
    @abstractmethod
    def __init__(self, sides, colour):
        pass # we never write any funcionality in the abstract
    @abstractmethod
    def num_sides(self):
        pass
    @abstractmethod
    def colour(self):
        pass


# We never instantiate abstract classes, 
# they are only ever used for inheritance




