from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Business(RootModel):
    """ business table definition """

    _tablename_ = "businesses"

    # fields of the businesses table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    business_type = db.Column(db.String(256), nullable=False, default="")
    age = db.Column(db.String(256), nullable=False, default="")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
