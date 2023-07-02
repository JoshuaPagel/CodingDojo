from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hi/<string:name>')
def greeting(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return f"{name * num}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)