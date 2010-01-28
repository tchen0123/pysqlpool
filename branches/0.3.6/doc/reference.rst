.. "reference.rst" file
.. moduleauthor:: NerdyNick <nerdynick@gmail.com>
.. sectionauthor:: NerdyNick <nerdynick@gmail.com>
.. sectionauthor:: NerdyNick <nerdynick@gmail.com>

===========================
PySQLPool Object Reference
===========================

:mod:`PySQLPool`
==================

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
=============================

The PySQLQuery class is by far one of the biggest work horses in the whole PySQLPool library, next to the PySQLPool class.
It is responsable for handaling the execution of your query(s). Which in itself is a lot of work. PySQLQuery handles talking 
to the heart of PySQLPool, The PySQLPool class. To fetch a new connection or one that has been estabished. It then creates a 
MySQL cursor object to handle the execution of your sql statement against your MySQL database. 

.. class:: PySQLQuery(PySQLConnectionObj[, commitOnEnd])

   .. attribute:: PySQLPool.PySQLQuery.Pool
   
       Used to store a reference to the PySQLPool object

   .. attribute:: PySQLPool.PySQLQuery.connInfo
   
       Used to store the connection information to be used for talking to the db. This is a PySQLConnection instance.

   .. attribute:: PySQLPool.PySQLQuery.commitOnEnd
   
       A boolean flag used to tell the connection that it should auto commit your statement at the end of its execution.

   .. attribute:: PySQLPool.PySQLQuery.record
   
       A storage reference to your results that where returned from your last select statement.

   .. attribute:: PySQLPool.PySQLQuery.rowcount
   
       The number of rows returned by your last select statement.

   .. attribute:: PySQLPool.PySQLQuery.affectedRows
   
       The number of affected rows that your last delete/insert/update statement affected.

   .. attribute:: PySQLPool.PySQLQuery.conn
   
       An internaly used reference to the current locked connection as returned by the PySQLPool class. This is an 
       instance of a PySQLConnectionManager object.

   .. attribute:: PySQLPool.PySQLQuery.lastError
   
       A reference to the last MySQL error as returned by the under lying MySQLdb library. You can reference this if you need. 
       But PySQLQuery will raise this error forward for you to catch yourself.

   .. attribute:: PySQLPool.PySQLQuery.lastInsertID
   
       The last auto incrament ID that an insert statement create.

   .. method:: PySQLPool.PySQLQuery.__del__()
   
       The destructor method used for freeing up any locked connections that may not have be release do to some reason. 

   .. method:: PySQLPool.PySQLQuery.query(query, *args)
   .. method:: PySQLPool.PySQLQuery.Query(query, *args) - Depracating to fit correct code standards.
   
       

   .. method:: PySQLPool.PySQLQuery.queryOne(query, *args)
   .. method:: PySQLPool.PySQLQuery.QueryOne(query, *args) - Depracating to fit correct code standards.

   .. method:: PySQLPool.PySQLQuery.executeMany(query, args)

   .. method:: PySQLPool.PySQLQuery.executeMulti(queries)

   .. method:: PySQLPool.PySQLQuery._GetConnection()

   .. method:: PySQLPool.PySQLQuery._ReturnConnection()

   .. method:: PySQLPool.PySQLQuery.escape_string()

   .. method:: PySQLPool.PySQLQuery.escape()



:mod:`PySQLPool.PySQLPool`
===========================

.. class:: PySQLPool()

   .. attribute:: PySQLPool.PySQLPool.__pool
    
   .. attribute:: PySQLPool.PySQLPool.maxActiveConnections
    
   .. attribute:: PySQLPool.PySQLPool.maxActivePerConnection
    
   .. method:: PySQLPool.PySQLPool.Terminate()
    
   .. method:: PySQLPool.PySQLPool.Cleanup()
    
   .. method:: PySQLPool.PySQLPool.Commit()
    
   .. method:: PySQLPool.PySQLPool.GetConnection(PySQLConnectionObj)
    
   .. method:: PySQLPool.PySQLPool.returnConnection(connObj)



:mod:`PySQLPool.PySQLConnection`
=================================

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