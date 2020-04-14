from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from src import estimator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save_estimation', methods=['GET', 'POST'])
def save_estimation():
    error = "Error submitting form..."
    if request.method == "POST":
        user_data = {
            "region": {
                "name": "Africa",
                "avgAge": 19.7,
                "avgDailyIncomeInUSD": 5,
                "avgDailyIncomePopulation": 0.71
            },
            "periodType": request.form["periodType"],
            "timeToElapse": int(request.form["timeToElapse"]),
            "reportedCases": int(request.form["reportedCases"]),
            "population": int(request.form["population"]),
            "totalHospitalBeds": int(request.form["totalHospitalBeds"])
        }
        estimator.estimator(user_data)
        return render_template('index.html')
    return render_template('index.html', error = error)    
if __name__ == '__main__':
    app.run(debug=True)