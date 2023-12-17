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

@departments_blueprint.route('/search_employee.html', methods=['POST'])
def search_department():
    idDepartment = request.form['idDepartment']
    try:
        department = Department.query.filter(department.idDepartment == idDepartment).first()
        return render_template('Website/success.html', title = "Department Found", department=department)
    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)

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
        return render_template('/Website/success.html', title = "Department Added", department=new_department)
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

#update department
@departments_blueprint.route('/update_department.html', methods=['POST'])
def update_department():
    idDepartment = request.form['newIdDepartment']

    try:
        department = Department.query.filter(Department.idDepartment==idDepartment).first()
        if 'newPositionName' in request.form and request.form['newPositionName'] != "":
            department.positionName = request.form['newPositionName']
        if 'newClassification' in request.form and request.form['newClassification'] != "":
            department.classification = request.form['newClassification']
        if 'newPrimaryLocation' in request.form and request.form['newPrimaryLocation'] != "":
            department.primaryLocation = request.form['newPrimaryLocation']

        db.session.commit()
        return render_template('Website/success.html', title = "Department Updated", department=department)
    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)
    