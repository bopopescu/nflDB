from flask import Flask, render_template, request, url_for, jsonify, json
from dbApp import config
from dbApp.db import *
from dbApp.functions import *


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/results', methods=['POST'])
def showResults():
	result = dbApp.db.query("SELECT * FROM company.employee")
	queryInput = request.form['query']
	return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
