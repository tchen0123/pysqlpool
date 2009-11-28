====================================
The PySQLPool.PySQLConnection Module
====================================

.. attribute:: connection_timeout

.. class:: PySQLConnection

   .. attribute:: info

   .. attribute:: key

   .. method:: __init__(*args, **kargs)

   .. method:: __getattr__(name)


.. class:: PySQLConnectionManager

   .. method:: __init__(PySQLConnectionObj)

   .. method:: updateCheckTime()

   .. method:: Connect()

   .. method:: ReConnect()

   .. method:: TestConnection(forceCheck = False)
   
   .. method:: Commit()
   
   .. method:: Close()