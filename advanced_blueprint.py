from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

advanced_blueprint = Blueprint('advanced_blueprint', __name__, template_folder='templates')
from flight_blueprint import Flight


@advanced_blueprint.route('/advanced.html', methods=['GET'])
def advanced_flight_form():
    return render_template('Website/advanced.html')

@advanced_blueprint.route('/advanced.html', methods=['POST'])
def advanced_flight():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    
    try:
        # Query flights within the specified period
        print("Trying to query flights...")
        flights = Flight.query.filter(Flight.departureDate.between(start_date, end_date)).all()
        print("Number of flights found:", len(flights))
        return render_template('Website/advanced.html', flights=flights)
    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/advanced.html', error_info=e)