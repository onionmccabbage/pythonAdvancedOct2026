# once we have a db with a table in it, we can populate the table with data

import sqlite3
from make_connection import makeConnection

def writeOneItem():
    '''Persist details of one creatre into the db table'''
    d = makeConnection()
    conn = d['conn'] # d[0] if its a tuple
    curs = d['curs']
    st = 'INSERT INTO zoo VALUES ("Penguin", 16, 0.52)'
    try:
        curs.execute(st)
        conn.commit()    # if we do not commit, then the changes will NOT persist
        conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    writeOneItem()
