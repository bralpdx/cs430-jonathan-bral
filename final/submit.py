from flask import Flask, redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Submit(MethodView):
    def post(self):
        """
        Accepts POST requests, processes the request,
        and then redirects to the Todo page
        """
        model = gbmodel.get_model()
        model.insert(request.form['title'], request.form['desc'], request.form['prio'])
        return redirect(url_for('todo'))
