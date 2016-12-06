from dbApp import config
from dbApp.db import *
from dbApp.functions import *







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

#Returns list of all positions 
def getAllPositions():
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
def getTeamPerformance(columns, team, year):
	statement = 'SELECT CONCAT(t.location, " ", t.team_name) as "Team Name", ' + ','.join([str(x) for x in columns]) + ' FROM NFLDB.team_season_performance s LEFT JOIN NFLDB.Teams t ON t.team_id = s.team_id WHERE season_id = '+ year + ' AND t.team_id = ' + team
	print(statement)
	result = dbApp.db.query(statement)
	result.append(statement)
	return result

#Get results for team information search
def getTeamInfo(team):
	string = "SELECT t.location, t.team_name, CONCAT(o.fname, ' ', o.lname) as 'Owner', l.league_name,CONCAT(c.fname, ' ', c.lname) as 'Coach' FROM NFLDB.Teams t LEFT JOIN NFLDB.owners o on o.owner_id = t.owner_id LEFT JOIN NFLDB.League  l on l.league_id = t.league_id LEFT JOIN NFLDB.Coach c ON c.coach_id = t.coach_id WHERE t.team_id = "+team;
	print(string)
	result = dbApp.db.query(string)
	result.append(string)
	return result


#Get results for player performance by team
def playerTeamPerformance(team,position,table,season):
	string = "SELECT CONCAT(pl.fname, ' ' ,pl.lname) as 'Name', CONCAT(t.location, ' ', t.team_name) as 'Team Name', p.* FROM %s p JOIN NFLDB.Players pl ON p.player_id = pl.player_id JOIN NFLDB.Teams t on pl.team_id = t.team_id WHERE pl.player_id in (SELECT player_id FROM NFLDB.Players WHERE team_id = %i ) AND p.season_id = %i"
	if position != "0":
		string += " AND pl.position_id = %s"
		result = dbApp.db.query(string, (table, team, season, position))
	else:
		result = dbApp.db.query(string, (table, team, season))
	result.append(string)
	return result