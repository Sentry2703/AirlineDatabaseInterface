from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

employees_blueprint = Blueprint('employee_blueprint', __name__, template_folder='templates')
from app import db

class Employee(db.Model):
    __tablename__ = 'Employee'
    idEmployee = db.Column(db.Integer, primary_key=True, unique=True)
    firstName = db.Column(db.String(45))
    lastName = db.Column(db.String(45))
    positionID = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    status = db.Column(db.Enum('Active', 'Retired', 'Vacationing', 'Fired'))

#Add Employee
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
        db.session.commit()
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

#Search Employee
@employees_blueprint.route('/search_employee.html')
def searchEmployee():
    return render_template('Website/search_employee.html')

@employees_blueprint.route('/search_employee.html', methods=['POST'])
def search_employee():
    idEmployee = request.form['employeeID']

    try:
        employee = Employee.query.filter(Employee.idEmployee==idEmployee).first()
        return render_template('Website/search_employee.html', employee=employee)
    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)


#update Employee
@employees_blueprint.route('/update_employee.html', methods=['POST'])
def update_employee():
    idEmployee = request.form['idEmployee']

    try:
        employee = Employee.query.filter(Employee.idEmployee==idEmployee).first()
        if 'New-FirstName' in request.form and request.form['New-FirstName'] != "":
            employee.firstName = request.form['New-FirstName']
        if 'New-LastName' in request.form and request.form['New-LastName'] != "":
            employee.lastName = request.form['New-LastName']
        if 'New-positionID' in request.form and request.form['New-positionID'] != "":
            employee.positionID = request.form['New-positionID']
        if 'New-Salary' in request.form and request.form['New-Salary'] != "":
            employee.salary = request.form['New-Salary']
        if 'New-Status' in request.form and request.form['New-Status'] != "":
            employee.status = request.form['New-Status']
        db.session.commit()

        employee = Employee.query.filter(Employee.idEmployee==idEmployee).first()
        return render_template('Website/search_employee.html', employee=employee)
    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)
    

#delete Employee
@employees_blueprint.route('/delete_employee.html', methods=['POST'])
def delete_employee():
    idEmployee = request.form['idEmployee']

    try:
        employee = Employee.query.filter(Employee.idEmployee==idEmployee).first()
        employee.status = "Fired"
        db.session.commit()
        return render_template('Website/search_employee.html', employee=employee)
    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)