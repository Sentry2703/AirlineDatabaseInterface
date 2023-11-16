from flask import Blueprint, render_template, request

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')

@search_blueprint.route('/search_employee.html', methods=['GET'])
def search_employee_form():
    return render_template('/Website/search_employee.html')

@search_blueprint.route('/search_results', methods=['POST'])
def search_results():
    search_employee_id = request.form['searchEmployee']

    from app import db

    class Employee(db.Model):
        __tablename__ = 'Employee'
        idEmployee = db.Column(db.Integer, primary_key=True, unique=True)
        firstName = db.Column(db.String(45))
        lastName = db.Column(db.String(45))
        positionID = db.Column(db.Integer)
        salary = db.Column(db.Integer)
        status = db.Column(db.Enum('Active', 'Retired', 'Vacationing', 'Fired'))

    try:
        search_result = Employee.query.filter_by(idEmployee=search_employee_id).first()

        if search_result:
            return render_template('Website/search_results.html', search_result=search_result)
        else:
            return render_template('Website/search_results.html', error_message='Employee not found.')

    except Exception as e:
        error_info = "An error occurred while processing your request."
        return render_template('Website/error.html', error_info=e)