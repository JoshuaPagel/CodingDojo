from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = "spaghetti"

@app.route('/')
def index():
    import random
    random.randint(1,100)
    return render_template("index.html")


if __name__ =="main":
    app.run(debug=True, port=5001)