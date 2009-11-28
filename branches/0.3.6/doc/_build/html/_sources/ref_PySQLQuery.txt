====================================
The PySQLPool.PySQLQuery Module
====================================

.. class:: PySQLQuery

   .. attribute:: Pool

   .. attribute:: connInfo

   .. attribute:: commitOnEnd

   .. attribute:: record

   .. attribute:: rowcount

   .. attribute:: affectedRows

   .. attribute:: conn

   .. attribute:: lastError

   .. attribute:: lastInsertID

   .. method:: __init__(PySQLConnectionObj, commitOnEnd = False)

   .. method:: __del__()

   .. method:: Query(query, *args)

   .. method:: QueryOne(query, *args)

   .. method:: executeMany(query, args)

   .. method:: executeMulti(queries)

   .. method:: _GetConnection()

   .. method:: _ReturnConnection()

   .. method:: escape_string()

   .. method:: escape()
      