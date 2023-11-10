from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Slentry2703@localhost/airport'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sentry2703@localhost:3306/airport'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('Website/add_plane.html')

@app.route('/add_plane.html')
def addPlane():
    return render_template('Website/add_plane.html')

@app.route('/add_employee.html')
def addEmployee():
    return render_template('Website/add_employee.html')


@app.route('/advanced.html')
def advanced():
    return render_template('Website/advanced.html')


@app.route('/create_department.html')
def create_department():
    return render_template('Website/create_department.html')


@app.route('/schedule_flight.html')
def schedule_flight():
    return render_template('Website/schedule_flight.html')


@app.route('/search_employee.html')
def searchEmployee():
    return render_template('Website/search_employee.html')

class Plane(db.Model):
    __tablename__ = 'Plane'
    idPlane = db.Column(db.String(45), primary_key=True, unique=True)
    capacity = db.Column(db.Integer)
    crewID = db.Column(db.Integer)  # Assuming this is a foreign key referencing another table
    planeType = db.Column(db.Enum('Private', 'Commercial', 'Jumbo', 'Cargo'))

@app.route('/add_plane.html', methods=['POST'])
def add_plane():
    idPlane = request.form['idPlane']
    capacity = request.form['capacity']
    crewID = request.form['crewID']
    planeType = request.form['planeType']

    new_plane = Plane(idPlane=idPlane, capacity=capacity, crewID=crewID, planeType=planeType)

    db.session.add(new_plane)
    try:
        db.session.commit()
    except Exception as e:
        print(f"Error committing to the database: {e}")
        db.session.rollback()  # Rollback changes to maintain database consistency
    finally:
        db.session.close()  # Close the session to release resources

    return redirect(url_for('addPlane'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
