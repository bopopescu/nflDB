from flask import Flask, render_template, request, url_for, jsonify, json,redirect
from dbApp import config
from dbApp.db import *
import os
import CONFIG   # Separate out per-machine configuration 


app = Flask(__name__)
app.debug=CONFIG.DEBUG
dbFunctions = dbApp.db.dbFunctions()

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/', methods=['GET','POST'])
def redirectPage():
	option = str(request.form.get("options"))
	return redirect('/'+option)

@app.route('/<page>Result', methods=['POST'])
def results(page):
	if page == 'teamPerf':
		teamId = request.form['options']
		year = request.form['years']
		columns = request.form.getlist("columnValue")
		results = dbFunctions.getTeamPerformance(columns,teamId,year)
		return render_template('results.html',result=results) 
	elif page == 'customQuery':
		query = request.form['query']
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif page == 'teamInfo':
		teamId = request.form['options']
		results = dbFunctions.getTeamInfo(teamId)
		return render_template('results.html',result=results) 
	elif page == 'playerTeamPerformance':
		teamId = request.form['team']
		posId = request.form['pos']
		table = request.form['table']
		results = dbFunctions.playerTeamPerformance(int(teamId),str(posId),str(table),2016)
		return render_template('results.html',result=results) 


@app.route('/<topStats>', methods=['GET','POST'])
def topPlayers(topStats):
	if topStats == 'passing':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,o.* FROM NFLDB.off_performance o JOIN NFLDB.Players p on o.player_id = p.player_id WHERE p.position_id = 'QB' ORDER BY o.passing_yds DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'rushing':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,o.* FROM NFLDB.off_performance o JOIN NFLDB.Players p on o.player_id = p.player_id WHERE p.position_id = 'RB' ORDER BY o.rush_yds DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'receiving':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,o.* FROM NFLDB.off_performance o JOIN NFLDB.Players p on o.player_id = p.player_id WHERE p.position_id = 'WR' ORDER BY o.receiving_yds DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'passingTD':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,o.* FROM NFLDB.off_performance o JOIN NFLDB.Players p on o.player_id = p.player_id WHERE p.position_id = 'QB' ORDER BY o.passing_td DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'rushingTD':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,o.* FROM NFLDB.off_performance o JOIN NFLDB.Players p on o.player_id = p.player_id WHERE p.position_id = 'RB' ORDER BY o.rushing_td DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'receivingTD':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,o.* FROM NFLDB.off_performance o JOIN NFLDB.Players p on o.player_id = p.player_id WHERE p.position_id = 'WR' ORDER BY o.receiving_td DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'tackles':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,d.* FROM NFLDB.def_performance d JOIN NFLDB.Players p on d.player_id = p.player_id ORDER BY d.tackles DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'interceptions':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,d.* FROM NFLDB.def_performance d JOIN NFLDB.Players p on d.player_id = p.player_id ORDER BY d.interceptions DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'fumble':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,d.* FROM NFLDB.def_performance d JOIN NFLDB.Players p on d.player_id = p.player_id ORDER BY d.forced_fumbles DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif topStats == 'fg':
		query = "SELECT CONCAT(p.fname, ' ' , p.lname) as 'Name' ,k.* FROM NFLDB.kicker_performance k JOIN NFLDB.Players p on k.player_id = p.player_id ORDER BY k.field_goal_made DESC LIMIT 20"
		results = dbFunctions.query(query)
		results.append(query)
		return render_template('results.html',result=results) 

@app.route('/Team-Performance')
def teamPerf():
	teams = dbFunctions.getAllTeams()
	return render_template('team.html',teams=teams)

@app.route('/Team-Information')
def teamInformation():
	teams = dbFunctions.getAllTeams()
	return render_template('teamInfo.html',teams=teams)

@app.route('/Custom-Query')
def customQuery():
	return render_template('customQuery.html')

@app.route('/Player-By-Team')
def playersByTeam():
	teams = dbFunctions.getAllTeams()
	positions = dbFunctions.getAllPositions()
	return render_template('players.html', positions = positions,teams=teams)


if __name__ == '__main__':
    app.run(port=CONFIG.PORT, debug=True, host="0.0.0.0")
