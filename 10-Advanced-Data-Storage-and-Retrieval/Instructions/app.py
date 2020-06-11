import datetime as dt
import numpy as np
import pandas as pd
import json

#My SQL Class I wrote
from sqlHelper import SQLHelper
from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################
@app.route("/api/v1.0/precipitation")
def get_total_precipitation():
    data = sqlHelper.getTotalPrecipOnDates()
    #convert to json string
    data = data.to_json(orient='records')
    #convert to list
    data = json.loads(data)
    #return jsonify
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def get_all_stations(): #insert a variable
    data = sqlHelper.getAllStationInformation()
    return(jsonify(json.loads(data.to_json(orient='records')))) #hack it all into one line

@app.route("/api/v1.0/tobs")
def get_temp_active_station(): #insert a variable
    data = sqlHelper.getTempForActiveStation()
    return(jsonify(json.loads(data.to_json(orient='records')))) #hack it all into one line

@app.route("/api/v1.0/temperature/<start>")
def get_temp_for_date(start): #insert a variable
    data = sqlHelper.getTempInfoForDate(start)
    return(jsonify(json.loads(data.to_json(orient='records')))) #hack it all into one line

@app.route("/api/v1.0/temperature/<start>/<end>")
def get_temp_for_date_range(start, end): #insert a variable
    data = sqlHelper.getTempInfoForDateRange(start, end)
    return(jsonify(json.loads(data.to_json(orient='records')))) #hack it all into one line

@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii Data API!<br/>"

        f"""
        <ul>
            <li><a target="_blank" href='/api/v1.0/precipitation'>Get Total Precipitation</a></li>
            <li><a target="_blank" href='/api/v1.0/stations'>Get All Stations</a></li>
            <li><a target="_blank" href='/api/v1.0/tobs'>Get Temperature for Most Active Station</a></li>
            <li><a target="_blank" href='/api/v1.0/temperature/2017-08-23'>Get Temperature for Date</a></li>
            <li><a target="_blank" href='/api/v1.0/temperature/2016-09-23/2017-05-23'>Get Temperature for Date Range</a></li>
        </ul>
        """
    )


#################################################
# Flask Run
#################################################
if __name__ == "__main__":
    app.run(debug= True)
