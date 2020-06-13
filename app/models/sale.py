from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Sale(RootModel):
    """ sale table definition """

    _tablename_ = "sales"

    # fields of the sales table
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(256), nullable=False, default="")
    quantity = db.Column(db.Integer, nullable=False, default=1)
    amount = db.Column(db.Integer, nullable=True, default=0)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
