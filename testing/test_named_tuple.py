# here we use pytest to test our named tuple
from collections import namedtuple
from the_named_tuple import Task

# use pytest
def test_members():
    t = Task('Finish doing stuff', 'Grace')
    # now we assert our tests
    assert t.summary == 'Finish doing stuff'
    assert t.owner   == 'Grace'
    assert t.done    == False # does this work...

if __name__ == '__main__':
    test_members() # here we invoke the tests