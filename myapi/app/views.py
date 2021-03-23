from app import app
from flask import jsonify
import os, requests
from flask import Flask, render_template, url_for, json
from healthcheck import HealthCheck


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def home():
   return "hello worldfasdsadsa"

@app.route('/meta')
def status(): 
   SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
   json_url = os.path.join(SITE_ROOT, "static/data", "metadata.json")
   data = json.load(open(json_url))
   return jsonify(data)

health = HealthCheck(app, "/healthcheck")

def healthy():
   return True, 'OK'

health.add_check(healthy)
