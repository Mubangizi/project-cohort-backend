import json
from flask_restful import Resource, request

from app.schemas import BusinessSchema
from app.models.business import Business



class BusinessView(Resource):

    def post(self):
        """
        Creating an Business ad
        """
        business_schema = BusinessSchema()

        business_data = request.get_json()

        validated_business_data, errors = business_schema.load(business_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        business = Business(**validated_business_data)

        saved_business = business.save()

        if not saved_business:
            return dict(status='fail', message='Internal Server Error'), 500

        new_business_data, errors = business_schema.dumps(business)

        return dict(status='success', data=dict(business=json.loads(new_business_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All businesses
        """

        business_schema = BusinessSchema(many=True)

        businesses = Business.find_all()

        businesses_data, errors = business_schema.dumps(businesses)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(businesses=json.loads(businesses_data))), 200


class BusinessDetailView(Resource):

    def get(self, business_id):
        """
        Getting individual business
        """
        schema = BusinessSchema()

        business = Business.get_by_id(business_id)

        if not business:
            return dict(status="fail", message=f"Business with id {business_id} not found"), 404

        business_data, errors = schema.dumps(business)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(business=json.loads(business_data))), 200

    def patch(self, business_id):
        """
        Update a single business
        """

        # To do check if user is admin
        schema = BusinessSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        business = Business.get_by_id(business_id)

        if not business:
            return dict(status="fail", message=f"Business with id {business_id} not found"), 404

        updated_business = Business.update(business, **validated_update_data)

        if not updated_business:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Business updated successfully"), 200

    def delete(self, business_id):
        """
        Delete a single business
        """

        business = Business.get_by_id(business_id)

        if not business:
            return dict(status="fail", message=f"Business with id {business_id} not found"), 404

        deleted_business = business.delete()

        if not deleted_business:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
