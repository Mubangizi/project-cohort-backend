from flask_restful import Api
from app.controllers import (IndexView, EmployeeView, EmployeeDetailView,
      TaskView, TaskDetailView, ConsultantView, ConsultantDetailView,
      SaleView, SaleDetailView, CourseView, CourseDetailView, AccountView,
      AccountDetailView, BusinessView, BusinessDetailView, UserView,
      UserDetailView, TicketView, TicketDetailView)



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
# sales
api.add_resource(SaleView, '/sales', endpoint='sales')
api.add_resource(SaleDetailView, '/sales/<int:sale_id>')
# courses
api.add_resource(CourseView, '/courses', endpoint='courses')
api.add_resource(CourseDetailView, '/courses/<int:course_id>')
# accounts
api.add_resource(AccountView, '/accounts', endpoint='accounts')
api.add_resource(AccountDetailView, '/accounts/<int:account_id>')
# businesses
api.add_resource(BusinessView, '/businesses', endpoint='businesses')
api.add_resource(BusinessDetailView, '/businesses/<int:business_id>')
# users
api.add_resource(UserView, '/users', endpoint='users')
api.add_resource(UserDetailView, '/users/<int:user_id>')
# tickets
api.add_resource(TicketView, '/tickets', endpoint='tickets')
api.add_resource(TicketDetailView, '/tickets/<int:ticket_id>')