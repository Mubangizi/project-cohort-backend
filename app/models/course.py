from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Course(RootModel):
    """ course table definition """

    _tablename_ = "courses"

    # fields of the courses table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    lecturer = db.Column(db.String(256), nullable=True, default="")
    code = db.Column(db.String(256), nullable=True, default="")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
