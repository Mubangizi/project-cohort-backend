from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Employee(RootModel):
    """ employee table definition """

    _tablename_ = "employees"

    # fields of the employees table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    salary = db.Column(db.Integer, nullable=False, default=1)
    age = db.Column(db.Integer, nullable=True, default=0)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return "<Employee: {}>".format(self.name)
