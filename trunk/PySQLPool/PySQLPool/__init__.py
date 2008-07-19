import PySQLConnection

def getNewConnection(host='localhost', username='root', password='', schema='', port=3306, commitOnEnd = False):
    return PySQLConnection.PySQLConnection(host=host, username = username,  password = password, schema = schema, port = port, commitOnEnd = commitOnEnd)

import PySQLQuery
def getNewQuery(connection = None, host='localhost', username='root', password='', schema='', port=3306, commitOnEnd = False):
    if connection is None:
        return PySQLQuery.PySQLQuery(getNewConnection(host=host, username = username,  password = password, schema = schema, port = port, commitOnEnd = commitOnEnd))
    else:
        return PySQLQuery.PySQLQuery(connection)

import PySQLPool
def getNewPool():
    return PySQLPool.PySQLPool()

def terminatePool():
    PySQLPool.PySQLPool().Terminate()