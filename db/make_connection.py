import sqlite3

def makeConnection(filename='my_db'):
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    # return (conn, curs) # tuple members 0, 1
    return {'conn':conn, 'curs':curs} # a dict

if __name__ == '__main__':
    makeConnection('my_db')