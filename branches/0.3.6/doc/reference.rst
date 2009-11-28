.. "reference.rst" file

===========================
PySQLPool Package Reference
===========================

.. attribute:: __version__
   
   PySQLPool Version Number

.. attribute:: __author__
   
   PySQLPool Author String

.. _getNewConnection:
.. method:: getNewConnection(*args, **kargs)
   
   Fast method to generate a new PySQLConnection instance. Arguments are those of PySQLConnection_

.. method:: getNewQuery(connection = None, commitOnEnd=False)
            getNewQuery(**kargs)
   
   Fast method to generate a new PySQLQuery instance.
   
   If an instance of a PySQLConnection object is passes for the connection parameter. It will be used for the 
   connection. Otherwise \**kargs will be used to generate a PySQLConnection instance via the getNewConnection_ method.

.. method:: getNewPool()
   
   Returns a reference to the current PySQLPool object

.. method:: terminatePool()
   
   Causes PySQLPool to commit and terminate all your current MySQL connections

.. method:: commitPool()
   
   Causes PySQLPool to commit all your current MySQL connections

.. method:: cleanupPool()
   
   Causes PySQLPool to analyse all current MySQL connections, and clean up an dead connections.
  
  
Modules
=======

.. toctree::
   :maxdepth: 3
   
   ref_PySQLConnection.rst
   ref_PySQLPool.rst
   ref_PySQLQuery.rst