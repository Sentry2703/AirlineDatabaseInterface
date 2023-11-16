from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

flights_blueprint = Blueprint('flights_blueprint', __name__, template_folder='templates')

from app import db

class Flight(db.Model):
    __tablename__ = 'Flight'
    idFlight = db.Column(db.Integer, primary_key=True, unique=True)
    destination = db.Column(db.String(45))
    planeID = db.Column(db.String(45))
    departureDate = db.Column(db.Date)
    departureTime = db.Column(db.Time)
    flightTime = db.Column(db.Integer)

@flights_blueprint.route('/schedule_flight.html')
def schedule_flight_form():
    return render_template('/Website/schedule_flight.html')

@flights_blueprint.route('/schedule_flight.html', methods=['POST'])
def schedule_flight():
    idFlight = request.form['idFlight']
    destination = request.form['destination']
    planeID = request.form['planeID']
    departureDate = request.form['departureDate']
    departureTime = request.form['departureTime']
    flightTime = request.form['FlightTime']

    new_flight = Flight(idFlight=idFlight, destination=destination, planeID=planeID, departureDate=departureDate, departureTime=departureTime, flightTime=flightTime)

    db.session.add(new_flight)
    try:
        print(1)
        db.session.commit()
        print(2)
        return redirect(url_for('flight_blueprint.schedule_flight_form'))
    except IntegrityError as e:
        db.session.rollback()
        error_info = str(e.orig)
        return render_template('Website/error.html', error_info=error_info)
    except Exception as e:
        db.session.rollback()
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)
    finally:
        pass