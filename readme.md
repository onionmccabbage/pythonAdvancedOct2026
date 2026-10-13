## Python Advanced

#### October 2026

Toby Dussek

#### You will need:
- Python 3.x
- an editor (e.g. VS Code, PyCharm etc.)
- internet, with permission to install python libraries (e.g. requests library)

#### Python code lives in classes (or in functions), in modules, which live in packages (folders)

* 9:30 start
* 11:00 break (15 mins)
* 12:00 lunch (1 hr)
* 3:00 break (15 minutes)
* 4:30 end

Course Repo https://github.com/onionmccabbage/pythonAdvancedOct2026

#### Monday
* intro and welcome
  - what you currently know
  - what you want to know 
* abstract and concrete classes
* class inheritance
* using slots
* Anything __nnn__ is a built in feature of Python. Called 'dunder'
* name-mangled members
* property decorators
* validate data types: isinstance, type, int(float())
* override built-in methods: __str__, __repr__, __eq__ etc.
* if __name__== '__main__'
* using sys.path
* after lunch review: build class(es) with properties and methods
* function parameters: args, kwargs
* functional programming: map, filter and reduce  

#### Tuesday
* how to accessing the recordings
  - https://learn.neueda.com/course/457328
  - Sign up with an email and password
  - when asked, enter code MHMZOD
* loading remote API data (requests)
  - pip install request   # or pip3 install requests
* persisting files: read/write/append/exclusive/overwrite, text, bytes, json
* processing text/json
* 'with' operator for clean handling of assets
* how to convert bytes back to string: b'this is bytes'.decode()
* Remember - in Python EVERYTHING is an OBJECT
* databases and SQL
    - see https://wiki.python.org/moin/DatabaseProgramming
* also useful: add 'sqlite viewer' plugin to VSCode
* see SQL tutorial https://www.w3schools.com/sql/
* Create, Read and Update (and Delete) - CRUD operations
* populate db with sample data
* read and nicely format values from the db
* after lunch review exercise

#### Wednesday
* comprehensions, generators and yield
* i/o bound: any program which relies on external assets (print, input....)
* python includes stdin and stdout
* redirect stdout
* context manager to switch context e.g. for handling data input and output
* networking server/client (microservices)
* Testing: (only really works if there is a good spec')
* doctest revisited
  see https://docs.python.org/3/library/doctest.html
  - unittest see https://docs.python.org/3/library/unittest.html
* pytest see https://docs.pytest.org/
* after lunch lab exercise
* Flask is a lightweight web server
  - django is a full-fat web server

#### Thursday
* classes include several really useful methods we may override:
  `__init__`, `__str__`, `__repr__`, `__enter__`, `__exit__`, `__run__`, `__call__`
* multithreading, also limits of mutlithreading concurrency
  * question: do __exit__ codes change with threading?
* class and function threads
  - how threads are done
* concurrency and resources (lock shared resources)
* async and await
* in Python we do not get true parallelism ...
  - the global Interpreter Lock (GIL)
  - Python 3.13+ contains an optional GIL
  - see https://peps.python.org/pep-0703/
* using thread locks
* Python has -O to optimize code 
  - (especially useful for threading and large code-base)
* profiling: timings etc. (cProfile)
* to use cProfile we write this:
  -  python -m cProfile -o prof_out using_api.py
* debug
* after lunch review
* async (Py3.12+) server and client for microservices
* Numpy and Pandas are written in c so they avoid the GIL
* the next course covers:
  - design patterns
  - extend threading and also multiprocessing
  - Numpy, Pandas and Data Analysis (jupyter)

where to go from here:
* use Python regularly
* work through the tutorials and exercises learnpython.org and pynative.com

End of course feedback 
