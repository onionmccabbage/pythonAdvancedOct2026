# There is a feature in Python called Named Tuple
from collections import namedtuple

# here we create a named tuple for 'Tasks'
# Named tuple is like a class but all its members are immutable
# Also, the order of the tuple matters and is labelled
Task = namedtuple('Task', ('summary', 'owner', 'done', 'id'))
# We have the option of specifying defaults for each member of our named tuple
Task.__new__.__defaults__ = (None, None, False, None)

# alternative syntax
def makeTaskTup( tup=tuple() ):
    '''we will define a named tuple to encapulate themembers of a task
    summary, owner, done, id
    We would normally validate these members'''
    task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
    task.__new__.__defaults__ = (None, None, False, None) # the None type is handy
    # we can unpack the members of the tup by using the asterisk *tup
    t = task(*tup)
    return t

if __name__ == '__main__':
    # we may create instances of our Task
    tX = Task('Learn Python', 'Oenid', False, 32)
    print(tX, type(tX))
    # Explore the defaults
    tD = Task() # use the default values
    print(tD)
    # can we skip defaults - only by specifying keyword arguments
    tZ = Task(summary='can we do this', id=32)
    print(tZ)