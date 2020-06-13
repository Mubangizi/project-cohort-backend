from flask_restful import Api
from app.controllers import (IndexView, EmployeeView, EmployeeDetailView,
      TaskView, TaskDetailView)



api = Api()

# Index route
api.add_resource(IndexView, '/')
# employees
api.add_resource(EmployeeView, '/employees', endpoint='employees')
api.add_resource(EmployeeDetailView, '/employees/<int:employee_id>')
# tasks
api.add_resource(TaskView, '/tasks', endpoint='tasks')
api.add_resource(TaskDetailView, '/tasks/<int:task_id>')