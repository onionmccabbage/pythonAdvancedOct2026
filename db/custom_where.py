# we can use parameters to update specific results from the db table
from make_connection import makeConnection

def updateData(w):
    '''update the values for specific items in the db table'''
    d = makeConnection()
    conn = d['conn'] # d[0] if its a tuple
    curs = d['curs']
    # retrieve the values from w
    creature = w['creature'] # we really should validate here
    count = w['count']
    # in SQL we use signle quotes for string values and NO QUOTES for numeric values
    st = f'''
    UPDATE zoo
    SET count = {count}
    WHERE creature = '{creature}'
'''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    # we could ask the user, or use sys.argv, or other means for the new data
    whichItem = {'creature':'Penguin', 'count':58}
    updateData(whichItem)