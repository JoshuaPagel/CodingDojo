from flask import Flask, render_template, session, request, redirect
app = Flask('__name__')
app.secret_key = "pizza"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods = ['POST'])
def results():
    print("post info")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route ('/results', methods = ['POST'])
def print_results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('results.html', name=name, location=location, language=language, comment=comment)


if __name__=='__main__':
    app.run(debug=True, port=5002)


# name=request.form['name'], location=request.form['location'], language = request.form['language'], comment = request.form['comment'])
# name = request.form['name']
    # location = request.form['location']
    # language = request.form['language']
    # comment = request.form['comment']
    # session['name'] = request.form['name']
    # session['location'] = request.form['location']
    # session['language'] = request.form['language']
    # session['comment'] = request.form['comment']
    # print(name, location, language, comment)
    # return render_template('results.html', name=request.form['name'], location=request.form['location'], language = request.form['language'], comment = request.form['comment'])