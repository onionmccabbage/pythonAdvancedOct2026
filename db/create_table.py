# Python comes with a business-quality database called sqlite3
# The principles are the same for any db engine

import sqlite3
from make_connection import makeConnection

def createTable():
    '''Create or open a database then make a table inside it'''
    d = makeConnection()
    conn = d['conn'] # d[0] if its a tuple
    curs = d['curs']
    # Next we write an SQL statement to create a table within this db
    st = 'CREATE TABLE IF NOT EXISTS zoo (creature VARCHAR(32) PRIMARY KEY, count int, cost float)'
    # implement the sql on the db
    try:
        curs.execute(st) # at this point no changes will happen
        conn.commit()    # here any db changes will be persisted
        conn.close()     # tidy up at the earliest opportunity. This releases resources
    except Exception as err:
        print(err)

if __name__ == '__main__':
    '''exercise this module'''
    createTable() # NB only need to run this once
