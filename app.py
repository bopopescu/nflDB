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


@app.route('/search', methods=['GET','POST'])
def showResults():
	option = str(request.form.get("options"))
	print(option)
	return redirect(url_for(option))

@app.route('/team')
def teamPerf():
	teams = dbApp.functions.getAllTeams()
	return render_template('team.html',teams=teams)



if __name__ == '__main__':
    app.run(port=8000, debug=True)
