====================================
The PySQLPool.PySQLConnection Module
====================================

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