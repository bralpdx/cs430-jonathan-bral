from flask import render_template
from flask.views import MethodView
import gbmodel

class Browse(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [
                dict(name=row[0], street=row[1], city=row[2], state=row[3], \
                zipcode=row[4], hours=row[5], phone=row[6], rating=row[7], review=row[8], \
                posted_on=row[9] ) for row in model.select()]
        return render_template('browse.html', entries=entries)
