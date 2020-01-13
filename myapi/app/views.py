from app import app
from flask import jsonify
import os
from flask import Flask, render_template, url_for, json

@app.route('/')
def home():
   return "hello worldi!"

@app.route('/status')
def status(): 
   SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
   json_url = os.path.join(SITE_ROOT, "static/data", "metadata.json")
   data = json.load(open(json_url))
   return jsonify(data)