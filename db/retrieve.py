import sqlite3

def retrieve():
    '''retrieve all items from the db table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # using * will select every field in the table
    st = 'SELECT * FROM zoo'
    try:
        curs.execute(st)
        conn.commit()    # we always commit, even if we make no changes to the db
        # we can now retrieve any values retured from the db
        rows = curs.fetchall() # retrieve zero or more results from the table
        conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    a = retrieve()
    print(a)