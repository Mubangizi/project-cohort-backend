from marshmallow import Schema, fields, validate


class ConsultantSchema(Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, error_message={
        "required": "name is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='name should be a valid string'
            ),
        ])
    field = fields.String()
    salary = fields.Integer(required=True, error_message={
        "required": "salary is required"})
    age = fields.Integer()
    