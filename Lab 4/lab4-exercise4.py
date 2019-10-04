import sqlite3

#Connect to database file
dbconnect = sqlite3.connect("my.db");

#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("my.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor()
cursor.execute('create TABLE sensors (sensorID INTEGER, temp FLOAT, date TEXT)')
dbconnect.commit()
#print data
print("(1)Display all sensors in the kitchen");
cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"');
for row in cursor:
     print(row['id'],row['type'],row['zone'] );
print("(2)Display all the door sensors");
cursor.execute('SELECT * FROM sensors WHERE type="door"');
for row in cursor:
     print(row['id'],row['type'],row['zone']);

#close the connection
dbconnect.close();
