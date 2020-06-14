from marshmallow import Schema, fields, validate


class SaleSchema(Schema):

    id = fields.Integer(dump_only=True)
    product = fields.String(required=True, error_message={
        "required": "product is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='product should be a valid string'
            ),
        ])
    quantity = fields.Integer(required=True, error_message={
        "required": "quantity is required"})
    amount = fields.Integer(required=True, error_message={
        "required": "amount is required"})
    