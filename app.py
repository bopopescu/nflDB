from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/results', methods=['POST'])
def showResults():
	query = request.form['query']
	return render_template('results.html', query=query)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
