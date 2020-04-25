from flask import render_template
from flask.views import MethodView

class Form(MethodView):
    def get(self):
        return render_template('sub_form.html')
