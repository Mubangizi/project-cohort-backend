from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db
from server import app

# import models
from app.models.employee import Employee
from app.models.task import Task
from app.models.consultant import Consultant
from app.models.sale import Sale
from app.models.course import Course


# register app and db with migration class
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()