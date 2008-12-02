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
    
    def __init__(self, commitOnEnd = False, *args, **kargs):
        """
        Constructor for the PySQLConnection class
        @param commitOnEnd: Default False, When query is complete do you wish to auto commit. This is a always on for this connection
        @author: Nick Verbeck
        @since: 5/12/2008
        @updated: 7/19/2008 - Added commitOnEnd
        @updated: 10/26/2008 - Switched to use *args and **kargs
        """
        self.info = {
                     'host': 'localhost',
                     'user': 'root',
                     'passwd': '',
                     'db': '',
                     'port': 3306
                     }
        if kargs.has_key('host'):
            self.info['host'] = kargs['host']
        if kargs.has_key('user'):
            self.info['user'] = kargs['user']
        if kargs.has_key('passwd'):
            self.info['passwd'] = kargs['passwd']
        if kargs.has_key('db'):
            self.info['db'] = kargs['db']
        if kargs.has_key('port'):
            self.info['port'] = int(kargs['port'])
            
        #Support Legacy Username
        if kargs.has_key('username'):
            self.info['user'] = kargs['username']
        #Support Legacy Password
        if kargs.has_key('password'):
            self.info['passwd'] = kargs['password']
        #Support Legacy Schema
        if kargs.has_key('schema'):
            self.info['db'] = kargs['schema']
            
        self.commitOnEnd = commitOnEnd
        hashStr = ''
        for key in self.info:
            hashStr += str(self.info[key])
        
        self.key = md5.new(hashStr).hexdigest()
        
    def __getattr__(self, name):
        try:
            return self.info[name]
        except Exception, e:
            return None
            


  
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
        self.connection = MySQLdb.connect(*[], **self.connectionInfo.info)
        
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