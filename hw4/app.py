"""
Foodcart gallery / rating system.
"""
import flask
from flask.views import MethodView
from index import Index
from browse import Browse
from form import Form
from submit import Submit

app = flask.Flask(__name__)       # our Flask app

"""
Function decorator === app.route('/',index())
"""

app.add_url_rule('/',
        view_func=Index.as_view('index'))

app.add_url_rule('/browse/',
        view_func=Browse.as_view('browse'),
        methods=['GET'])

app.add_url_rule('/form/',
        view_func=Form.as_view('form'))

app.add_url_rule('/submit/',
        view_func=Submit.as_view('submit'),
        methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
