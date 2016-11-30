from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='ix.cs.uoregon.edu',port=8080, debug=True)
