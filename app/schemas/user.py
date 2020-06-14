from marshmallow import Schema, fields, validate


class UserSchema(Schema):

    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, error_message={
        "required": "username is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='username should be a valid string'
            ),
        ])
    email = fields.String(required=True, error_message={
        "required": "User email is required"})
    gender = fields.String(required=True, error_message={
        "required": "Gender is required"})
    Address = fields.String()
    