import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

#reflect existing database into a new model
Base=automap_base()

Base.prepare(engine,reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Set-up

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    #Create session from Python to the DB
    session=Session(engine)

    #Query preciptation
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).all()

    session.close()
    #Create dictionary 
    all_precipitation = []
    for date, precipitation in results:
        precip_results ={}
        precip_results["date"] = date
        precip_results["precipitation"] = prcp
        all_precipitation.append(precip_results)

    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)

    results = session.query(Measurement.station).group_by(Measurement.station).all()

    session.close()

    stations = list(np.ravel(results))

    retirm jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)
    
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    results=sesion.query(Measurment.date, Measurement.tobs).filter(Measurement.station=="USC00519281").filter(Measurement.date >= query_date).all()
    
    all_tobs = []
    for date, tobs in results:
        tobs_results = {}
        tobs_results["date"] = date
        tobs_results["tobs"] = tobs
        all_tobs.append(tobs_results)
    return jsonify(all_precipitation)

@app.route("/api/v1.0/<start>")
def start_date(start):
    for date in Station:


