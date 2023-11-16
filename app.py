from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Slentry2703@localhost/airport'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sql242@localhost:3306/airport'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import plane_blueprint
app.register_blueprint(plane_blueprint.planes_blueprint, name='plane_blueprint')
import employee_blueprint
app.register_blueprint(employee_blueprint.employees_blueprint, name='employee_blueprint')
import department_blueprint
app.register_blueprint(department_blueprint.departments_blueprint, name='department_blueprint')
import flight_blueprint
app.register_blueprint(flight_blueprint.flights_blueprint, name='flight_blueprint')

@app.route('/advanced.html')
def advanced():
    return render_template('Website/advanced.html')


@app.route('/search_employee.html')
def searchEmployee():
    return render_template('Website/search_employee.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
