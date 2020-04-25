"""
A simple guestbook flask app.
"""
from flask import Flask, redirect, request, url_for, render_template

#from model_sqlite3 import model
from model_pylist import model

app = Flask(__name__)       # our Flask app
model = model()

"""
Function decorator === app.route('/',index())
"""
@app.route('/')
@app.route('/index.html')
def index():
    """
    Functions as default main page.
    """
    return render_template('index.html')

@app.route('/browse.html')
def browse():
    """
    Lists cart entries.
    """
    entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3] ) for row in model.select()]
    return render_template('browse.html', entries=entries)

@app.route('/sub_form.html')
def form():
    """
    Page for submitting new entries.
    """
    return render_template('sub_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Accepts POST requests, and processes the form;
    Adds new cart (entry) to db.
    Redirect to form when completed.
    """
    model.insert(request.form['name'], request.form['email'], request.form['message'])
    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
