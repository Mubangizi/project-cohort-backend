from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class User(RootModel):
    """ user table definition """

    _tablename_ = "users"

    # fields of the users table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), nullable=False, default="")
    email = db.Column(db.String(256), nullable=False, default="")
    gender = db.Column(db.String(256), nullable=False, default="")
    address = db.Column(db.String(256), nullable=False, default="")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
