
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = '172672834'

@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/result', methods=['Post'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favLang'] = request.form['favLang']
    session['comment'] = request.form['comment']
    return render_template("submit.html")
if __name__=="__main__":
    app.run(debug=True)
