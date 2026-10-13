# here we invoke from the other db modules
from create_table import createTable
from populate import writeOneItem
from populate_many import populateMany
from retrieve import retrieve

import sys

# it is a common enough convention to call the module (and function) 'main'
def main():
    '''Carry out SQL db operations based on user choice
    Check if there is an additional system argument valriable and use it if so
    If not, ask the user which option'''
    optlimits = '1-4'
    if len(sys.argv) > 1: # remember there is always sys.argv[0] which is the module name
        option = sys.argv[1]
        print(f'Option is: {option}') # NB every sys.argv is ALWAYS a string value
    else:
        print( '1 create table, 2 write one, 3 write many, 4 retrieve all' )
        option = input('Please choose an option (1-4)')
    # validate the option
    if option.isnumeric():
        optnum = int(float(option)) # arguably float is redundant here
    else:
        raise TypeError('Option must be numeric')
    # act upon the options
    match optnum: # we may use match-case from Python 3.10 onwards
        case 1:
            createTable()
        case 2:
            writeOneItem()
        case 3:
            populateMany()
        case 4:
            a = retrieve() # we actually retrieve from the db
            print(a)
        case _:
            raise TypeError(f'Option must be {optlimits}')

if __name__ == '__main__':
    main()
