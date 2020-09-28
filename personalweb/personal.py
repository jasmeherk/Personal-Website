from flask import Flask, render_template,url_for,request, session, g, flash, jsonify
import sys
import json
import pandas as pd  

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.debug=True
	app.run()