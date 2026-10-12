# all parts of Python are based on the object class

e = list()

# some validation techniques
a = 1
b = 4.3
c = 'lunch'
d = '1.234'
e = '23235'

print( isinstance(a, int) ) # True
print( type(b) ) # float
print( int(float(d)) ) # make the string into a float, then an int
# be careful with the following:
print( d.isnumeric() )
print( e.isnumeric() ) # isnumeric can ONLY contain digits
print( d.isdecimal() )
print( e.isdecimal() )