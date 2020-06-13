from flask_restful import Api
from app.controllers import (IndexView, EmployeeView, EmployeeDetailView)



api = Api()

# Index route
api.add_resource(IndexView, '/')
api.add_resource(EmployeeView, '/employees', endpoint='employees')
api.add_resource(EmployeeDetailView, '/employees/<int:employee_id>')