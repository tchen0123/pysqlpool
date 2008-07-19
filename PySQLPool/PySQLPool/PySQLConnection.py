"""
@author: Nick Verbeck
@since: 5/12/2008
"""

import md5

class PySQLConnection(object):
    """
    Command Pattern Object to store connection information for use in PySQLPool
    
    @author: Nick Verbeck
    @since: 5/12/2008
    @version: 0.1
    """
    
    def __init__(self, host='localhost', username='root', password='', schema='', port=3306, commitOnEnd = False):
        """
        Constructor for the PySQLConnection class
        
        @param host: Hostname for your database
        @param username: Username to use to connect to database
        @param password: Password to use to connect to database 
        @param schema: Schema to use
        @param port: Port to connect on
        @param commitOnEnd: Default False, When query is complete do you wish to auto commit.
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        self.host = host
        self.username = username
        self.password = password
        self.schema = schema
        self.port = port
        self.commitOnEnd = commitOnEnd
        
        self.key = md5.new(str(self.host) + str(self.username) + str(self.password) + str(self.schema) + str(self.port) + str(self.commitOnEnd)).hexdigest()


  
import sys, MySQLdb
from threading import Condition

class PySQLConnectionManager:
    """
    Physical Connection manager
    
    Used to manage the physical MySQL connection and the thread safe locks on that connection
    
    @author: Nick Verbeck
    @since: 5/12/2008
    @version: 0.1
    """
    def __init__(self, PySQLConnectionObj):
        """
        Constructor for PySQLConnectionManager
        
        @param PySQLConnectionObj: PySQLConnection Object representing your connection string
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        
        self.connectionInfo = PySQLConnectionObj
        self.connection = None
        self.lock = Condition()
        self.activeConnections = 0
        self.query = None
        self.Connect()
        
    def Connect(self):
        """
        Creates a new physical connection to the database
        
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        self.connection = MySQLdb.connect(host=self.connectionInfo.host, 
                                          user=self.connectionInfo.username, 
                                          passwd=self.connectionInfo.password, 
                                          db=self.connectionInfo.schema,
                                          port=self.connectionInfo.port)
        
    def ReConnect(self):
        """
        Attempts to close current connection if open and re-opens a new connection to the database
        
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        self.Close()
        self.Connect()
        
    def TestConnection(self):
        """
        Tests the current physical connection if it is open and hasn't timed out
        
        @return: boolean True is connection is open, False if connection is closed
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        if self.connection is None:
            return False
        else:
            try:
                cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('select current_user')
                return True
            except Exception, e:
                self.connection = None
                return False
            
    def Commit(self):
        """
        Commit MySQL Transaction to database
        
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        try:
            self.connection.commit()
        except Exception, e:
            pass
    
    def Close(self):
        """
        Commits and closes the current connection
        
        @author: Nick Verbeck
        @since: 5/12/2008
        """
        if self.connection is not None:
            try:
                self.connection.commit()
                self.connection.close()
                self.connection = None
            except Exception, e:
                pass