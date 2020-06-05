import flask
from flask.views import MethodView
from index import Index
from todo import Todo
from submit import Submit
from delete import Delete

app = flask.Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'))

app.add_url_rule('/todo/',
        view_func=Todo.as_view('todo'),
        methods=['GET'])

app.add_url_rule('/submit/',
        view_func=Submit.as_view('submit'),
        methods=['POST'])

app.add_url_rule('/delete/',
        view_func=Delete.as_view('delete'),
        methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
