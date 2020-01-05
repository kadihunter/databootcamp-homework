import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt
#import numpy as np

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"To obtain precipitation data for the last year data was available<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"To determine what stations have been compiling data within the API<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"To obtain temperature data for the highest reporting station for the last year data was available<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"To obtain the minimum, average and maximum temperatures from 'YYYY-MM-DD' until the most recent data<br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"<br/>"
        f"To obtain the minimum, average and maximum temperatures from 'YYYY-MM-DD' until 'YYYY-MM-DD'<br/>"
        f"i.e. 2015-08-05 to 2016-04-03 would be /api/v1.0/2015-08-05/2016-04-03<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all preciptation for every location"""
    # Query to determine last data point
    lastdate = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    
    #Calculate one year ago's date
    year = dt.datetime.strptime(lastdate[0], '%Y-%m-%d')
    sub_years = year - dt.timedelta(days=366)
    
    #Query all precipitation points for 1 year
    yearppt = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date > sub_years).order_by(Measurement.date).all()


    session.close()


    precip = []
    for date, prcp in yearppt:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip.append(precip_dict)


    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all station names
    stationname = session.query(Station.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers

    return jsonify(stationname)
    
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all tobs data for most active location"""
    
    # Query to determine last data point
    lastdate = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    
    #Calculate one year ago's date
    year = dt.datetime.strptime(lastdate[0], '%Y-%m-%d')
    sub_years = year - dt.timedelta(days=366)
    
    # Query all temperature points for 1 year
    stationname = session.query(Station.name, func.count(Measurement.station)).\
        filter(Measurement.station == Station.station).group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).all()
    activedata = stationname[0][0]
    yeartemp = session.query(Measurement.tobs).\
        filter(Measurement.date > sub_years).filter(Station.name == activedata).all()

    session.close()

    return jsonify(yeartemp)   
    

@app.route("/api/v1.0/<start>")
def star_temps(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    tempdata = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
        
    session.close()

    #results = jsonify(tempdata)
    #tempmin = results[0]
    #tempave = results[1]
    #tempmax = results[2]

    return jsonify(tempdata)
    #(
    #    f"The minimum temperature was 'tempmin' <br/>"
    #    f"The average temperature was 'tempave' <br/>"
    #    f"The maximum temperature was 'tempmax' <br/>"
    #    )
   
   
@app.route("/api/v1.0/<start>/<end>")
def between_temps(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    tempdata = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()
    
    return jsonify(tempdata)


if __name__ == '__main__':
    app.run(debug=True)
