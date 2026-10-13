import sqlite3

def retrieve():
    '''retrieve all items from the db table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # using * will select every field in the table
    st = 'SELECT * FROM zoo'
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