from flask import Flask, render_template, request, url_for, jsonify, json,redirect
from dbApp import config
from dbApp.db import *
from dbApp.functions import *


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html') 


@app.route('/<page>Result', methods=['POST'])
def results(page):
	if page == 'teamPerf':
		teamId = request.form['options']
		year = request.form['years']
		columns = request.form.getlist("columnValue")
		results = dbApp.functions.getTeamPerformance(columns,teamId,year)
		return render_template('results.html',result=results) 
	elif page == 'customQuery':
		query = request.form['query']
		results = dbApp.db.query(query)
		results.append(query)
		return render_template('results.html',result=results) 
	elif page == 'teamInfo':
		teamId = request.form['options']
		results = dbApp.functions.getTeamInfo(teamId)
		return render_template('results.html',result=results) 
	elif page == 'playerTeamPerformance':
		teamId = request.form['team']
		posId = request.form['pos']
		table = request.form['table']
		print(teamId,posId,table)
		results = dbApp.functions.playerTeamPerformance(int(teamId),str(posId),str(table),2016)
		return render_template('results.html',result=results) 

@app.route('/', methods=['GET','POST'])
def showPage():
	option = str(request.form.get("options"))
	print(option)
	return redirect(url_for(option))


@app.route('/team')
def teamPerf():
	teams = dbApp.functions.getAllTeams()
	return render_template('team.html',teams=teams)

@app.route('/teamInfo')
def teamInformation():
	teams = dbApp.functions.getAllTeams()
	return render_template('teamInfo.html',teams=teams)

@app.route('/custom')
def customQuery():
	return render_template('customQuery.html')

@app.route('/playersByTeam')
def playersByTeam():
	teams = dbApp.functions.getAllTeams()
	positions = dbApp.functions.getAllPositions()
	return render_template('players.html', positions = positions,teams=teams)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
