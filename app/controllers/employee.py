import json
from flask_restful import Resource, request

from app.schemas import EmployeeSchema
from app.models.employee import Employee



class EmployeeView(Resource):

    def post(self):
        """
        Creating an Employee ad
        """
        employee_schema = EmployeeSchema()

        employee_data = request.get_json()

        validated_employee_data, errors = employee_schema.load(employee_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        employee = Employee(**validated_employee_data)

        saved_employee = employee.save()

        if not saved_employee:
            return dict(status='fail', message='Internal Server Error'), 500

        new_employee_data, errors = employee_schema.dumps(employee)

        return dict(status='success', data=dict(employee=json.loads(new_employee_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All employees
        """

        employee_schema = EmployeeSchema(many=True)

        employees = Employee.find_all()

        employees_data, errors = employee_schema.dumps(employees)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(employees=json.loads(employees_data))), 200


class EmployeeDetailView(Resource):

    def get(self, employee_id):
        """
        Getting individual employee
        """
        schema = EmployeeSchema()

        employee = Employee.get_by_id(employee_id)

        if not employee:
            return dict(status="fail", message=f"Employee with id {employee_id} not found"), 404

        employee_data, errors = schema.dumps(employee)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(employee=json.loads(employee_data))), 200

    def patch(self, employee_id):
        """
        Update a single employee
        """

        # To do check if user is admin
        schema = EmployeeSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        employee = Employee.get_by_id(employee_id)

        if not employee:
            return dict(status="fail", message=f"Employee with id {employee_id} not found"), 404

        updated_employee = Employee.update(employee, **validated_update_data)

        if not updated_employee:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Employee updated successfully"), 200

    def delete(self, employee_id):
        """
        Delete a single employee
        """

        employee = Employee.get_by_id(employee_id)

        if not employee:
            return dict(status="fail", message=f"Employee with id {employee_id} not found"), 404

        deleted_employee = employee.delete()

        if not deleted_employee:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
