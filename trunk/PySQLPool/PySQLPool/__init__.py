import PySQLConnection

def getNewConnection(host='localhost', username='root', password='', schema='', port=3306):
    return PySQLConnection.PySQLConnection(host=host, username = username,  password = password, schema = schema, port = port)

import PySQLQuery
def getNewQuery(connection = None, host='localhost', username='root', password='', schema='', port=3306):
    if connection is None:
        return PySQLQuery.PySQLQuery(getNewConnection(host=host, username = username,  password = password, schema = schema, port = port))
    else:
        return PySQLQuery.PySQLQuery(connection)

import PySQLPool
def getNewPool():
    return PySQLPool.PySQLPool()

def terminatePool():
    PySQLPool.PySQLPool().Terminate()