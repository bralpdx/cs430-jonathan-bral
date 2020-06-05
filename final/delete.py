from flask import Flask, redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Delete(MethodView):
    def post(self):
        model = gbmodel.get_model()
        model.delete_task(request.form['title'], request.form['prio'])
        return redirect(url_for('todo'))
