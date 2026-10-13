import sqlite3
from make_connection import makeConnection

def retrieve():
    '''retrieve all items from the db table'''
    d = makeConnection()
    conn = d['conn'] # d[0] if its a tuple
    curs = d['curs']
    # using * will select every field in the table
    # Alternatively we may choose which columns and which order to retrieve
    st = 'SELECT creature, count, cost FROM zoo'
    try:
        curs.execute(st)
        # conn.commit() # if there is no change to the db we don't need to commit
        # we can now retrieve any values retured from the db
        rows = curs.fetchall() # retrieve zero or more results from the table
        conn.close()
        return rows
    except Exception as err:
        print(err)

if __name__ == '__main__':
    a = retrieve()
    print(a)