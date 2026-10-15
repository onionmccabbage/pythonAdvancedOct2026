# https://www.geeksforgeeks.org/python/__exit__-in-python/

class Divide:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    # we may choose to override the default __enter__ and __exit__
    def __enter__(self):
        print('Inside __enter__')
    def __exit__(self, exc_type, exc, tb):
        print('Inside __exit__')
        print(f'Exception type:{exc_type}')
        print(f'Exception value:{exc}')
        print(f'Traceback:{tb}')
    def divide_by_zero(self):
        # causes ZeroDivisionError exception
        print(self.num1 / self.num2)

if __name__ == '__main__':
    r1= Divide(3,1)
    with r1:
        r1.divide_by_zero() #3
    print('.'*68)
    # will raise a ZeroDivisionError
    r2 = Divide(3,0)
    with r2:
        r2.divide_by_zero()