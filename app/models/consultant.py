from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Consultant(RootModel):
    """ consultant table definition """

    _tablename_ = "consultants"

    # fields of the consultants table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    field = db.Column(db.String(256), nullable=False, default="")
    age = db.Column(db.Integer, nullable=True, default=0)
    salary = db.Column(db.Integer, nullable=True, default=0)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return "<Consultant: {}>".format(self.name)
