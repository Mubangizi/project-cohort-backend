from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Account(RootModel):
    """ account table definition """

    _tablename_ = "accounts"

    # fields of the accounts table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    number = db.Column(db.String(500), nullable=False, default="")
    bank = db.Column(db.String(256), nullable=True, default="")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
