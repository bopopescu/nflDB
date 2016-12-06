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


class dbFunctions:
	#Custom query
	def query(self, query='', parameters=()):
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

	#Returns list of all teams 
	def getAllTeams(self):
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

	#Returns list of all positions 
	def getAllPositions(self):
		cnx = mysql.connector.connect(**configDB)
		string = 'SELECT pos_id, position_name FROM NFLDB.positions'
		if cnx.is_connected():
			print('database connection established.')
			pass
		else:
			print('database connection failed.')
		cursor = cnx.cursor()
		cursor.execute(string)
		result = cursor.fetchall()
		return result

	#Get results for team performance search
	def getTeamPerformance(self,columns, team, year):
		statement = 'SELECT CONCAT(t.location, " ", t.team_name) as "Team Name", ' + ','.join([str(x) for x in columns]) + ' FROM NFLDB.team_season_performance s LEFT JOIN NFLDB.Teams t ON t.team_id = s.team_id WHERE season_id = '+ year + ' AND t.team_id = ' + team
		result = self.query(statement)
		result.append(statement)
		return result

	#Get results for team information search
	def getTeamInfo(self,team):
		string = "SELECT t.location, t.team_name, CONCAT(o.fname, ' ', o.lname) as 'Owner', l.league_name,CONCAT(c.fname, ' ', c.lname) as 'Coach' FROM NFLDB.Teams t LEFT JOIN NFLDB.owners o on o.owner_id = t.owner_id LEFT JOIN NFLDB.League  l on l.league_id = t.league_id LEFT JOIN NFLDB.Coach c ON c.coach_id = t.coach_id WHERE t.team_id = "+team;
		result = self.query(string)
		result.append(string)
		return result


	#Get results for player performance by team
	def playerTeamPerformance(self,team,position,table,season):
		string = "SELECT CONCAT(pl.fname, ' ' ,pl.lname) as 'Name', CONCAT(t.location, ' ', t.team_name) as 'Team Name', p.* FROM %s p JOIN NFLDB.Players pl ON p.player_id = pl.player_id JOIN NFLDB.Teams t on pl.team_id = t.team_id WHERE pl.player_id in (SELECT player_id FROM NFLDB.Players WHERE team_id = %i ) AND p.season_id = %i"
		if position != "0":
			string += " AND pl.position_id = '%s'"
			result = self.query(string % (table, team, season, position))
			string = string % (table, team, season, position)
		else:
			result = self.query(string % (table, team, season))
			string = string % (table, team, season)
		if len(result) == 0:
			result.append([])
		result.append(string)
		return result
