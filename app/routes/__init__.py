from flask_restful import Api
from app.controllers import (IndexView, EmployeeView, EmployeeDetailView,
      TaskView, TaskDetailView, ConsultantView, ConsultantDetailView)



api = Api()

# Index route
api.add_resource(IndexView, '/')
# employees
api.add_resource(EmployeeView, '/employees', endpoint='employees')
api.add_resource(EmployeeDetailView, '/employees/<int:employee_id>')
# tasks
api.add_resource(TaskView, '/tasks', endpoint='tasks')
api.add_resource(TaskDetailView, '/tasks/<int:task_id>')
# consultants
api.add_resource(ConsultantView, '/consultants', endpoint='consultants')
api.add_resource(ConsultantDetailView, '/consultants/<int:consultant_id>')