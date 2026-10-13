# here we will place several more reates into the db table

import sqlite3

def populateMany():
    conn = sqlite3.connect('my_db')
    curs = conn.curs()
    # here we use ? to stand in for each item value
    st = 'INSERT INTO zoo VALUES (?, ?, ?)'
    for item in creature_tuple:
        try:
            # using sql '?' lets us validate each member against SQL attacks
            curs.execute(st, (item['creature'], item['count'], item['cost']) )
            conn.commit() # we commit each change in turn
        except Exception as err:
            print(err)
    conn.close()

if __name__ == '__main__':
    creature_tuple = ( # normally this data would come from an API, a file, a microservice etc.
        {'creature':'Albatros', 'count':1,   'cost':120.99},
        {'creature':'Bear',     'count':5,   'cost':120.99},
        {'creature':'Carp',     'count':120, 'cost':120.99},
        {'creature':'Deer',     'count':32,  'cost':120.99},
        {'creature':'Elk',      'count':7,   'cost':120.99},
    )
    # run our function
    populateMany()