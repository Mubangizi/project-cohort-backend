from marshmallow import Schema, fields, validate


class CourseSchema(Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, error_message={
        "required": "product is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='product should be a valid string'
            ),
        ])
    code = fields.String(required=True, error_message={
        "required": "course code is required"})
    lecturer = fields.String(required=True, error_message={
        "required": "lecturer is required"})
    