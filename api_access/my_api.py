# We may request external data from a REST API

import requests # may need to pip install requests

def getJSON():
    '''retrieve JSON data as Python structures'''
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url) # or POST, PUT etc.
    # NB the next line retrieves teh text JSON and converts it to Python structures
    data = response.json() # or .text or xml etc
    return data

if __name__ == '__main__':
    d = getJSON()
    print(d, type(d))


