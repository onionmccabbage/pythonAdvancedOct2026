# There is a feature in Python called Named Tuple
from collections import namedtuple

# here we create a named tuple for 'Tasks'
# Named tuple is like a class but all its members are immutable
# Also, the order of the tuple matters and is labelled
Task = namedtuple('Task', ('summary', 'owner', 'done', 'id'))
# We have the option of specifying defaults for each member of our named tuple
Task.__new__.__defaults__ = (None, None, False, None)

if __name__ == '__main__':
    # we may create instances of our Task
    tX = Task('Learn Python', 'Oenid', False, 32)
    print(tX, type(tX))
    # Explore the defaults
    tD = Task() # use the default values
    print(tD)