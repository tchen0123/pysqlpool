.. "reference.rst" file
.. moduleauthor:: NerdyNick <nerdynick@gmail.com>
.. sectionauthor:: NerdyNick <nerdynick@gmail.com>
.. sectionauthor:: NerdyNick <nerdynick@gmail.com>

:mod:`PySQLPool` - PySQLPool Package Structure
==============================================

.. attribute:: PySQLPool.__version__
   
   PySQLPool Version Number

.. attribute:: PySQLPool.__author__
   
   PySQLPool Author String

.. _getNewConnection:
.. function:: PySQLPool.getNewConnection(*args, **kargs)
   
   Fast function to generate a new PySQLConnection instance. Arguments are those of PySQLConnection_

.. function:: PySQLPool.getNewQuery([connection[, commitOnEnd[, **kargs]]])
   
   Fast method to generate a new PySQLQuery instance.
   
   If an instance of a PySQLConnection object is passes for the connection parameter. It will be used for the 
   connection. Otherwise \**kargs will be used to generate a PySQLConnection instance via the getNewConnection_ method.

.. function:: PySQLPool.getNewPool()
   
   Returns a reference to the current PySQLPool object

.. function:: PySQLPool.terminatePool()
   
   Causes PySQLPool to commit and terminate all your current MySQL connections

.. function:: PySQLPool.commitPool()
   
   Causes PySQLPool to commit all your current MySQL connections

.. function:: PySQLPool.cleanupPool()
   
   Causes PySQLPool to analyse all current MySQL connections, and clean up an dead connections.
  


:mod:`PySQLPool.PySQLQuery`
===========================

.. class:: PySQLQuery(PySQLConnectionObj[, commitOnEnd])

   .. attribute:: Pool

   .. attribute:: connInfo

   .. attribute:: commitOnEnd

   .. attribute:: record

   .. attribute:: rowcount

   .. attribute:: affectedRows

   .. attribute:: conn

   .. attribute:: lastError

   .. attribute:: lastInsertID

   .. method:: __del__()

   .. method:: Query(query, *args)

   .. method:: QueryOne(query, *args)

   .. method:: executeMany(query, args)

   .. method:: executeMulti(queries)

   .. method:: _GetConnection()

   .. method:: _ReturnConnection()

   .. method:: escape_string()

   .. method:: escape()
      
 :mod:`PySQLPool.PySQLPool`
===========================

 .. class:: PySQLPool()

    .. attribute:: __pool
    
    .. attribute:: maxActiveConnections
    
    .. attribute:: maxActivePerConnection
    
    .. method:: Terminate()
    
    .. method:: Cleanup()
    
    .. method:: Commit()
    
    .. method:: GetConnection(PySQLConnectionObj)
    
    .. method:: returnConnection(connObj)
    
 :mod:`PySQLPool.PySQLConnection`
===========================

.. attribute:: connection_timeout

A `datetime.timedelta` representing your default MySQL connection_timeout. This is used 
to improve performance with checking to see if connections are valid and reconnecting if needed. Each
connection instance maintains a timestamp of its last activity. That is updated for every query or test.
The connection is auto tested for every new instance of a PySQLQuery created on its initial fetching 
of a connection.

.. class:: PySQLConnection([host, [user, [passwd, [db, [port]]]]])
	
	Command Pattern Object to store connection information for use in PySQLPool

   .. attribute:: info
   
   Dictionary containing the connection info to be passed off to the MySQLdb layer

   .. attribute:: key
   
   An auto generated md5 checksum to represent your connection in the pool. This is generated off of the
   username, password, host, and db/schema.

   .. method:: __getattr__(name)


.. class:: PySQLConnectionManager

   .. method:: __init__(PySQLConnectionObj)

   .. method:: updateCheckTime()

   .. method:: Connect()

   .. method:: ReConnect()

   .. method:: TestConnection(forceCheck = False)
   
   .. method:: Commit()
   
   .. method:: Close()