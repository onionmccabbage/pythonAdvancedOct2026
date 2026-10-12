from abc import ABCMeta, abstractmethod

class ABCReview(metaclass=ABCMeta):
    # we may include __slots__ here
    __slots__ = ('__n',) 
    @property
    @abstractmethod
    def n(self, n):
        pass
    @abstractmethod
    def __str__(self):
        pass