from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        """
        Functions as default main page.
        """
        return render_template('index.html')

