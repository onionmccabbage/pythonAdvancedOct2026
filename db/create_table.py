# Python comes with a business-quality database called sqlite3
# The principles are the same for any db engine

import sqlite3

def createTable():
    '''Create or open a database then make a table inside it'''
    # we need a connection to a db. This is I/O bound
    conn = sqlite3.connect('my_db') # if it doesnt exist it will be created. If it already exists conn will connect to it
    # we then need a cursor to work with the database
    curs = conn.cursor()
    # Next we write an SQL statement to create a table within this db
    st = 'CREATE TABLE zoo (creature VARCHAR(32) PRIMARY KEY, count int, cost float)'
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
