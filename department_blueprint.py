from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError


departments_blueprint = Blueprint('departments_blueprint', __name__, template_folder='templates')

from app import db
    
class Department(db.Model):
    __tablename__ = 'Department'
    idDepartment = db.Column(db.Integer, primary_key=True, unique=True)
    positionName = db.Column(db.String(45))
    classification = db.Column(db.Enum(('Air Crew','Janitorial','Concessions','Management')))
    primaryLocation = db.Column(db.String(45)) 
    
@departments_blueprint.route('/create_department.html')
def create_department():
    return render_template('/Website/create_department.html')

@departments_blueprint.route('/create_department.html', methods=['POST'])
def add_department():
    idDepartment = request.form['idDepartment']
    positionName = request.form['positionName']
    classification = request.form['classification']
    primaryLocation = request.form['primaryLocation']

    new_department = Department(idDepartment=idDepartment, positionName=positionName, classification=classification, primaryLocation=primaryLocation)

    
    try:
        db.session.add(new_department)
        print(1)
        db.session.commit()
        print(2)
        return redirect(url_for('department_blueprint.create_department'))
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