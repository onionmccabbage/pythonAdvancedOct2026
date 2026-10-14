# here we use pytest to test our named tuple
from collections import namedtuple
from the_named_tuple import Task

# use pytest
def test_members():
    t = Task('Finish doing stuff', 'Grace')
    # now we assert our tests
    assert t.summary == 'Finish doing stuff'
    assert t.owner   == 'Grace'
    assert (t.done, t.id) == (False, None) # note when we imported Task it also got the default

def testDefaults():
    t = Task()
    s = Task(None, None, False, None)
    assert t==s

if __name__ == '__main__':
    test_members() # here we invoke the tests