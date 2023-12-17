from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

planes_blueprint = Blueprint('planes_blueprint', __name__, template_folder='templates')

from app import db

class Plane(db.Model):
    __tablename__ = 'Plane'
    idPlane = db.Column(db.String(45), primary_key=True, unique=True)
    capacity = db.Column(db.Integer)
    crewID = db.Column(db.Integer) 
    planeType = db.Column(db.Enum('Private', 'Commercial', 'Jumbo', 'Cargo'))

@planes_blueprint.route('/')
def index():
    return render_template('/Website/add_plane.html')

@planes_blueprint.route('/add_plane.html', methods=['GET'])
def add_plane_form():
    return render_template('/Website/add_plane.html')

@planes_blueprint.route('/add_plane.html', methods=['POST'])
def add_plane():
    idPlane = request.form['idPlane']
    capacity = request.form['capacity']
    crewID = request.form['crewID']
    planeType = request.form['planeType']
    new_plane = Plane(idPlane=idPlane, capacity=capacity, crewID=crewID, planeType=planeType)

    db.session.add(new_plane)
    try:
        print(1)
        db.session.commit()
        print(2)
        return render_template('/Website/success.html', title = "Plane Added", plane=new_plane)
    except IntegrityError as e:
        print(3)
        db.session.rollback()
        print(4)
        error_info = str(e.orig)
        print(5)
        return render_template('Website/error.html', error_info=error_info)
    except Exception as e:
        print(6)
        db.session.rollback()
        print(7)
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)
    finally:
        pass

#update plane
@planes_blueprint.route('/update_plane.html', methods=['POST'])
def update_plane():
    planeID = request.form['planeID']

    try:
        plane = Plane.query.filter(Plane.planeID == planeID).first()
        if 'newCapacity' in request.form and 'newCapacity' != "":
            plane.capacity = request.form['newCapacity']
        if 'newCrewID' in request.form and 'newCrewID' != "":
            plane.crewID = request.form['newCrewID']
        if 'newPlaneType' in request.form and 'newPlaneType' != "":
            plane.status = request.form['newPlaneType']

        db.session.commit()
        plane = Plane.query.filter(Plane.planeID == planeID).first()
        return render_template('/Website/sucess.html', title = "Plane Updated", plane=plane)
    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)