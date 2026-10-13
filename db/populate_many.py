# here we will place several more reates into the db table

import sqlite3
from make_connection import makeConnection

def populateMany():
    d = makeConnection()
    conn = d['conn'] # d[0] if its a tuple
    curs = d['curs']
    # here we use ? to stand in for each item value
    # suppose one of the ? was '0 where 0=0 drop table'
    st = 'INSERT INTO zoo VALUES (?, ?, ?)'
    for item in creature_tuple:
        try:
            # using sql '?' lets us validate each member against SQL attacks
            creature = item['creature']
            if type(creature)==str and creature != '':
                pass
            else:
                raise TypeError('Creature name must be a non-empty sting')
            count = item['count']
            if type(count) == int and count >=0:
                pass
            else:
                raise TypeError('Creature count must be a positive integer')
            cost = item['cost']
            if type(cost) in (int, float) and cost >=0:
                pass
            else:
                raise TypeError('Creature cost must be a positive number')           
            curs.execute(st, (creature, count, cost) )
            conn.commit() # we commit each change in turn
        except Exception as err:
            print(err)
    conn.close()

creature_tuple = ( # normally this data would come from an API, a file, a microservice etc.
    {'creature':'Albatros', 'count':1,   'cost':120.99},
    {'creature':'Bear',     'count':5,   'cost':120.99},
    {'creature':'Carp',     'count':120, 'cost':120.99},
    {'creature':'Deer',     'count':32,  'cost':120.99},
    {'creature':'Elk',      'count':7,   'cost':120.99},
)
if __name__ == '__main__':
    # run our function
    populateMany()