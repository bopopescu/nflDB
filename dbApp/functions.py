from dbApp import config
from dbApp.db import *
from dbApp.functions import *





#Select statement builder
def getTeamPerformance(columns, team, year):
	statement = 'SELECT CONCAT(t.location, " ", t.team_name) as "Team Name", ' + ','.join([str(x) for x in columns]) + ' FROM NFLDB.team_season_performance JOIN NFLDB.Teams t ON t.team_id = '+ team
	print(statement)
	result = dbApp.db.query(statement)
	result.append(statement)
	return result

#Returns list of all teams 
def getAllTeams():
	cnx = mysql.connector.connect(**configDB)
	string = 'SELECT CONCAT(t.location, " ", t.team_name), t.team_id FROM NFLDB.Teams t'
	if cnx.is_connected():
		print('database connection established.')
		pass
	else:
		print('database connection failed.')
	cursor = cnx.cursor()
	cursor.execute(string)
	result = cursor.fetchall()
	return result
