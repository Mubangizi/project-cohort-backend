from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Task(RootModel):
    """ task table definition """

    _tablename_ = "tasks"

    # fields of the tasks table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    description = db.Column(db.String(256), nullable=False, default="")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return "<Task: {}>".format(self.name)
