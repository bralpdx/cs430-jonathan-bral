from flask import Flask, redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Submit(MethodView):
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirects to form page when completed.
        """
        model = gbmodel.get_model()
        model.insert(
                request.form['name'], request.form['street'],
                request.form['city'], request.form['state'],
                request.form['zipcode'], request.form['hours'],
                request.form['phone'], request.form['rating'],
                request.form['review'])
        return redirect(url_for('form'))
