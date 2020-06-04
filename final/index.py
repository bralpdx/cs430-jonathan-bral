from flask import render_template
from flask.views import MethodView
import os
import json
import requests
import weather

class Index(MethodView):
    def get(self):
        forecast = weather.get_weather()
        return render_template('index.html', forecast=forecast)
