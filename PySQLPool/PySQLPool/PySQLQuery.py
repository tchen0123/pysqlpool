"""
@author: Nick Verbeck
@since: date 5/12/2008
"""

import thread, time, md5, MySQLdb, sys
from PySQLPool import PySQLPool

class PySQLQuery(object):
    """
    Front-End class used for interaction with the PySQLPool core
    
    This class is used to execute queries and to request a currently open connection from the pool. 
    If no open connections exist a new one is created by the pool.
    
    @author: Nick Verbeck
    @since: 5/12/2008
    @version: 0.1
    """
    
    def __init__(self, PySQLConnectionObj, commitOnEnd = False):
        """
        Constructor for PySQLQuery Class
        
        @param PySQLConnectionObj: PySQLConnection Object representing your connection string
        @param commitOnEnd: Default False, When query is complete do you wish to auto commit. This is a one time auto commit
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        self.Pool = PySQLPool()
        self.connInfo = PySQLConnectionObj
        self.commitOnEnd = commitOnEnd
        self.record = {}
        self.rowcount = 0
        self.affectedRows = 0
        self.conn = None
        
    def __del__(self):
        """
        On destruct make sure the current connection is returned back to the pool for use later
        
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        if self.conn is not None:
            self.Pool.returnConnection(self.conn)
        
    def Query(self, query, args = None):
        """
        Execute the passed in query against the database
        
        @param query: MySQL Query to execute. %s or %(key)s will be replaced by parameter args sequence
        @param args: Sequence of value to replace in your query. A mapping may also be used but your query must use %(key)s
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        
        #Attempt to get a connection. If all connections are in use and we have reached the max number of connections,
        #we wait 1 second and try again.
        while self.conn is None:
            self.conn = self.Pool.GetConnection(self.connInfo)
            if self.conn is not None:
                break
            else:
                time.sleep(1)
                
        try:
            #Acquire Connection Lock to be thread safe
            self.conn.lock.acquire()
            
            #Test if connection is still active. If not reconnect.
            if self.conn.TestConnection() is False:
                self.conn.ReConnect()
            
            self.conn.query = query
            
            #Execute query and store results
            cursor = self.conn.connection.cursor(MySQLdb.cursors.DictCursor)
            self.affectedRows = cursor.execute(query, args)
            self.rowcount = cursor.rowcount
            
            self.record = cursor.fetchall()
            
            cursor.close()
        except Exception, e:
            pass
        finally:
            if self.connInfo.commitOnEnd is True or self.commitOnEnd is True:
                self.conn.Commit()
                
            self.Pool.returnConnection(self.conn)
            self.conn.lock.release()
            self.conn = None