from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def first_level():
    return render_template("playground.html", num=3, color="orange")

@app.route('/play/<int:num>')
def second_level(num):
    return render_template("playground.html", num=num, color="orange")

@app.route('/play/<int:num>/<string:color>')
def third_level(num, color):
    return render_template("playground.html", num=num, color=color)

if __name__=='__main__':
    app.run(debug=True, port=8000)
