from flask import Flask, request, redirect, url_for, render_template
from flask.views import MethodView
import gbmodel
import os
import random
import openweather

API_KEY = os.environ['OPEN_KEY']

class Todo(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(title=row[0], desc=row[1], prio=row[2]) for row in model.select()]
        offset = random.randint(0,50)
        return render_template('todo.html', entries=entries)
