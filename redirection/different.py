# we may alter ANY feature of Python

class OddAddEven(): # we may inherit from int, float or str with their default __add__ behaviours
    '''This class represents a numer, but when added,
      the result will ALWAYS be an even number'''
    # here  we modify the behaviour of __add__
    def __init__(self, value):
        self.num = value
    # we may override the default behaviour of addition
    def __add__(self, other):
        '''add the values, check if odd, add 1 if needed'''
        result = self.num + other.num
        if result/2 == result//2:
            return result
        else:
            if result<0:
                return result-1 # for negative numbers
            else:
                return result+1

# __eq__ equality
# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    '''exercise this module'''
    n1 = OddAddEven(-2)
    n2 = OddAddEven(-3)
    print(n1+n2) # -4
