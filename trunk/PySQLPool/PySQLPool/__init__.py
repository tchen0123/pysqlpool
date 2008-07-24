import PySQLConnection

def getNewConnection(host='localhost', username='root', password='', schema='', port=3306, commitOnEnd = False):
    """
    Quickly Create a new PySQLConnection class
    
    @param host: Hostname for your database
    @param username: Username to use to connect to database
    @param password: Password to use to connect to database 
    @param schema: Schema to use
    @param port: Port to connect on
    @param commitOnEnd: Default False, When query is complete do you wish to auto commit. This is a always on for this connection
    @author: Nick Verbeck
    @since: 5/12/2008
    @updated: 7/19/2008 - Added commitOnEnd support
    """
    return PySQLConnection.PySQLConnection(host=host, username = username,  password = password, schema = schema, port = port, commitOnEnd = commitOnEnd)

import PySQLQuery
def getNewQuery(connection = None, host='localhost', username='root', password='', schema='', port=3306, commitOnEnd = False):
    """
    Create a new PySQLQuery Class
    
    @param PySQLConnectionObj: PySQLConnection Object representing your connection string
    @param commitOnEnd: Default False, When query is complete do you wish to auto commit. This is a one time auto commit
    @author: Nick Verbeck
    @since: 5/12/2008
    @updated: 7/19/2008 - Added commitOnEnd support
    """
    if connection is None:
        return PySQLQuery.PySQLQuery(getNewConnection(host=host, username = username,  password = password, schema = schema, port = port), commitOnEnd = commitOnEnd)
    else:
        #Updated 7/24/08 to include commitOnEnd here
        #-Chandler Prall
        return PySQLQuery.PySQLQuery(connection, commitOnEnd = commitOnEnd)

import PySQLPool
def getNewPool():
    """
    Create a new PySQLPool
    
    @author: Nick Verbeck
    @since: 5/12/2008
    """
    return PySQLPool.PySQLPool()

def terminatePool():
    """
    Terminate all Connection
    
    @author: Nick Verbeck
    @since: 5/12/2008
    """
    PySQLPool.PySQLPool().Terminate()