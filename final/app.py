import flask
from flask.views import MethodView
from index import Index
from todo import Todo

app = flask.Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'))

app.add_url_rule('/todo/',
        view_func=Todo.as_view('todo'),
        methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
