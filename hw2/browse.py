from flask import render_template
from flask.views import MethodView
import gbmodel

class Browse(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(name=row[0], phone=row[1], signed_on=row[2], review=row[3] ) for row in model.select()]
        return render_template('browse.html', entries=entries)
