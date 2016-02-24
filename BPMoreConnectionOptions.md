**The wiki docs are being depricated. Please refer to http://packages.python.org/PySQLPool for documentation**

# Blueprint: more-connection-options #

Documentation/Spec for blueprint [more-connection-options](https://blueprints.launchpad.net/pysqlpool/+spec/more-connection-options)


# Details #

Replace keyed arguments in PySQLConnection with dynamic arguments (**args &****kargs). These will be used to allow for a user to pass more arguments to MySQLdb. They will also be taken into account when creating the Connection Hash used in PySQLPool.**

To note this will also cause PySQLConnection to have to use the same keyed aguments as MySQLdb. So legacy support for username(user), password(pass), and schema(db) will need to be added.