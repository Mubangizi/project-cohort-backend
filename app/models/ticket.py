from datetime import timedelta

from ..models import db

from app.models.root_model import RootModel


class Ticket(RootModel):
    """ ticket table definition """

    _tablename_ = "tickets"

    # fields of the tickets table
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(256), nullable=False, default="")
    location = db.Column(db.String(256), nullable=False, default="")
    on = db.Column(db.String(256), nullable=False, default="")
    tickets_available = db.Column(db.Integer, nullable=False, default=0)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
