from marshmallow import Schema, fields, validate


class BusinessSchema(Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, error_message={
        "required": "name is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='name should be a valid string'
            ),
        ])
    business_type = fields.String(required=True, error_message={
        "required": "Account name is required"})
    age = fields.String()
    