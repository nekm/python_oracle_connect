#!Mario Maruševec 26.11.2019 
# primjer spajanja na Oracle bazu

import sys
import cx_Oracle
import db_config

def printf (format,*args):
  sys.stdout.write (format % args)

def printException (exception):
  error, = exception.args
  printf ("Error code = %s\n",error.code);
  printf ("Error message = %s\n",error.message);

try:
  
  connection = cx_Oracle.Connection("%s/%s@%s" % (db_config.username,db_config.password,db_config.databasename)) 
  #connection = cx_Oracle.Connection("%s/%s@%s" % (username,password,databasename)) 
except cx_Oracle.DatabaseError as exc:
  printf ('Failed to connect to %s\n',db_config.databasename)
  printException (exc)
  exit (1)

cursor = connection.cursor ()
sql = """
  SELECT TABLE_NAME, TABLESPACE_NAME 
  from SYS.USER_TABLES
  --where LOAD_ID = :load
  ORDER BY 1 ASC"""

try:
  cursor.execute (sql)##, load = 1
except cx_Oracle.DatabaseError as exc:
  printf ('Failed to select \n')
  printException (exc)
  exit (1)

#result = cursor.fetchall ()
for TABLE_NAME, TABLESPACE_NAME in cursor.fetchall ():
  printf (" %s,  %s\n",TABLE_NAME, TABLESPACE_NAME)

cursor.close ()

connection.close ()

exit (0)