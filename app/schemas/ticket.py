from marshmallow import Schema, fields, validate


class TicketSchema(Schema):

    id = fields.Integer(dump_only=True)
    event = fields.String(required=True, error_message={
        "required": "event is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='event should be a valid string'
            ),
        ])
    location = fields.String(required=True, error_message={
        "required": "Location is required"})
    on = fields.String(required=True, error_message={
        "required": "event date is required"})
    tickets_available = fields.Integer()
    