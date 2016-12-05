from flask import Flask, render_template, request, url_for, jsonify, json,redirect
from dbApp import config
from dbApp.db import *
from dbApp.functions import *


app = Flask(__name__)


@app.route('/team')
def teamPerformance():
	teams = dbApp.db.getAllTeams()
	return render_template('team.html',teams=teams)

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/search', methods=['GET','POST'])
def showResults():
	option = str(request.form.get("options"))
	return redirect(url_for(option))



if __name__ == '__main__':
    app.run(port=8000, debug=True)
