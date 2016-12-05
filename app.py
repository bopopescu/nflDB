from flask import Flask, render_template, request, url_for, jsonify, json,redirect
from dbApp import config
from dbApp.db import *
from dbApp.functions import *


app = Flask(__name__)


@app.route('/team')
def Team():
	return render_template('team.html')

@app.route('/')
def hello():
    return render_template('index.html') 


@app.route('/search', methods=['GET','POST'])
def showResults():
	option = str(request.form.get("options"))
	return redirect(url_for(option))

	# page = option.lower() + '.html'
	# return render_template(page) 







if __name__ == '__main__':
    app.run(port=8000, debug=True)
