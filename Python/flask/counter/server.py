from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key = "testing"

@app.route('/')
def home_page():
    if "counter" not in session:
        session["counter"] = 0
    session["counter"] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

# @app.route('/add')
# def add():
#     session["counter"] += 1
#     return redirect('/')

# if 'key_name' in session:
#     print('key exists!')
# else:
#     print("key 'key_name' does NOT exist")

if __name__ =="__main__":
    app.run(debug=True, port=5001)