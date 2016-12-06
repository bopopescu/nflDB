import dbApp.config
import mysql.connector
from mysql.connector import errorcode, errors
from datetime import date, datetime, timedelta

configDB = {	
	'user': dbApp.config.DBuser,
	'password': dbApp.config.DBpassword,
	'host': dbApp.config.DBhost,
	'port': dbApp.config.DBport,
	'database': dbApp.config.DBdatabase,
	'raise_on_warnings': dbApp.config.DBraise_on_warnings,
	'autocommit': dbApp.config.DBautocommit# ,
}

#Custom query
def query(query='', parameters=()):
	cnx = mysql.connector.connect(**configDB)
	print(query)
	print(parameters)
	if cnx.is_connected():
		print('database connection established.')
		pass
	else:
		print('database connection failed.')
	cursor = cnx.cursor()
	cursor.execute(query, parameters)
	columns = [desc[0] for desc in cursor.description]
	columnValues = cursor.fetchall()
	if len(columnValues) == 0:
		return []
	else:
		values = []
		for row in columnValues:
			row = dict(zip(columns, row))
			values.append(row)
		result = []
		result.append(columns)
		result.append(values)
		cnx.close()
		return result

