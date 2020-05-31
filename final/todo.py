from flask import render_template
from flask.views import MethodView

class Todo(MethodView):
    def get(self):
        return render_template('todo.html')
    def post(self):
        return render_template('todo.html')
