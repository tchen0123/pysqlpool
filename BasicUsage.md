**The wiki docs are being depricated. Please refer to http://packages.python.org/PySQLPool for documentation**

How to use PySQLPool

# Introduction #

This is a basic example of how to us PySQLPool in your application.

# Example #
```
import PySQLPool

connection = PySQLPool.getNewConnection(host = 'localhost', username='user', password='pass', schema='mysql')
query = PySQLPool.getNewQuery(connection = connection)
query.Query("YOUR SQL")
for row in query.record:
   row['COLUMN NAME']
```

# Details #

PySQLPool.getNewConnection() returns a new PySQLConnection class. This class is used as a means of storing your connection information in a commonly accessible pattern withing PySQLPool. You can destroy and recreate as many of these classes as you wish. It will not effect the performance of PySQLPool.

Once you have a PySQLConnection object you can now request a new PySQLQuery Object. This is the object that will do all our work for you. Pass it the connection object and run all the queries you wish to execute against that connection. If you wish to change schemes or databases you will need to request a new connection object and a new query object to execute against.