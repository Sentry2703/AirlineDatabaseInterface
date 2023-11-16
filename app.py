from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sentry2703@localhost/airport'
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
import advanced_blueprint
app.register_blueprint(advanced_blueprint.advanced_blueprint, name='advanced_blueprint')


@app.route('/search_employee.html')
def searchEmployee():
    return render_template('Website/search_employee.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
