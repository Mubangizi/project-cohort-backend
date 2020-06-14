import json
from flask_restful import Resource, request

from app.schemas import SaleSchema
from app.models.sale import Sale



class SaleView(Resource):

    def post(self):
        """
        Creating an Sale ad
        """
        sale_schema = SaleSchema()

        sale_data = request.get_json()

        validated_sale_data, errors = sale_schema.load(sale_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        sale = Sale(**validated_sale_data)

        saved_sale = sale.save()

        if not saved_sale:
            return dict(status='fail', message='Internal Server Error'), 500

        new_sale_data, errors = sale_schema.dumps(sale)

        return dict(status='success', data=dict(sale=json.loads(new_sale_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All sales
        """

        sale_schema = SaleSchema(many=True)

        sales = Sale.find_all()

        sales_data, errors = sale_schema.dumps(sales)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(sales=json.loads(sales_data))), 200


class SaleDetailView(Resource):

    def get(self, sale_id):
        """
        Getting individual sale
        """
        schema = SaleSchema()

        sale = Sale.get_by_id(sale_id)

        if not sale:
            return dict(status="fail", message=f"Sale with id {sale_id} not found"), 404

        sale_data, errors = schema.dumps(sale)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(sale=json.loads(sale_data))), 200

    def patch(self, sale_id):
        """
        Update a single sale
        """

        # To do check if user is admin
        schema = SaleSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        sale = Sale.get_by_id(sale_id)

        if not sale:
            return dict(status="fail", message=f"Sale with id {sale_id} not found"), 404

        updated_sale = Sale.update(sale, **validated_update_data)

        if not updated_sale:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Sale updated successfully"), 200

    def delete(self, sale_id):
        """
        Delete a single sale
        """

        sale = Sale.get_by_id(sale_id)

        if not sale:
            return dict(status="fail", message=f"Sale with id {sale_id} not found"), 404

        deleted_sale = sale.delete()

        if not deleted_sale:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
