import os
import cities
from datetime import datetime
from flask import Flask, render_template, request,jsonify

tmpl_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=tmpl_dir)

'''
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
'''

japan_cities = getattr(cities,"cities")

@app.route('/')
def index():
    #script="./static/leaflet-0.7.3/leaflet.js"
    #css="./static/leaflet-0.7.3/leaflet.css"
    title = "Japan Tsunami Map"
    return render_template('index.html',title=title,japancities=japan_cities)

@app.route('/tsunami',methods=["POST"])
def tsunami():
    lon = request.form["lon"]
    lat = request.form["lat"]
    dat = request.form["date"]
    return jsonify(status="node_down",node="todo")


if __name__ == "__main__":
    app.run()

