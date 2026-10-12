# Python has built in tools to work with JSON data
import json

# JSON is fundamentally text (i.e. a string)
j = '''[
  {
    "userId": 1,
    "id": 1,
    "title": "must use double quotes",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": false
  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": true
  },
  {
    "userId": 1,
    "id": 5,
    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
    "completed": false
  },
  {
    "userId": 1,
    "id": 6,
    "title": "qui ullam ratione quibusdam voluptatem quia omnis",
    "completed": false
  }
]'''

# use the json library
o = json.loads(j) # json.loads will attempt to convert the JSON into Python structures
print(o)
print(type(o)) # we have a Python list
print(o[4], type(o[4])) # a dict
print( o[4]['title'] )

# we can convert any Python structure to JSON
people = [{'name':'Timnit Gebru', 'admin':True, 'age':39}, {'name':'Floella Benjamin', 'admin':False, 'age':72}]
t = json.dumps(people)
print(type(t)) # str