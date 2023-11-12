from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from app import db

employees_blueprint = Blueprint('employee_blueprint', __name__, template_folder='templates')


class Employee(db.Model):
    __tablename__ = 'Employee'
    idEmployee = db.Column(db.Integer, primary_key=True, unique=True)
    firstName = db.Column(db.String(45))
    lastName = db.Column(db.String(45))
    positionID = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    status = db.Column(db.Enum('Active', 'Retired', 'Vacationing', 'Fired'))

@employees_blueprint.route('/add_employee.html', methods=['GET'])
def add_employee_form():
    return render_template('/Website/add_employee.html')

@employees_blueprint.route('/add_employee.html', methods=['POST'])
def add_employee():
    idEmployee = request.form['idEmployee']
    firstName = request.form['FirstName']
    lastName = request.form['LastName']
    positionID = request.form['positionID']
    salary = request.form['Salary']
    status = request.form['Status']

    new_employee = Employee(idEmployee=idEmployee, firstName=firstName, lastName=lastName, positionID=positionID, salary=salary, status=status)

    db.session.add(new_employee)
    try:
        print(1)
        db.session.commit()
        print(2)
        return redirect(url_for('employee_blueprint.add_employee_form'))
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
