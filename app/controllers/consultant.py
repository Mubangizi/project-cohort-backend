import json
from flask_restful import Resource, request

from app.schemas import ConsultantSchema
from app.models.consultant import Consultant



class ConsultantView(Resource):

    def post(self):
        """
        Creating an Consultant ad
        """
        consultant_schema = ConsultantSchema()

        consultant_data = request.get_json()

        validated_consultant_data, errors = consultant_schema.load(consultant_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        consultant = Consultant(**validated_consultant_data)

        saved_consultant = consultant.save()

        if not saved_consultant:
            return dict(status='fail', message='Internal Server Error'), 500

        new_consultant_data, errors = consultant_schema.dumps(consultant)

        return dict(status='success', data=dict(consultant=json.loads(new_consultant_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All consultants
        """

        consultant_schema = ConsultantSchema(many=True)

        consultants = Consultant.find_all()

        consultants_data, errors = consultant_schema.dumps(consultants)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(consultants=json.loads(consultants_data))), 200


class ConsultantDetailView(Resource):

    def get(self, consultant_id):
        """
        Getting individual consultant
        """
        schema = ConsultantSchema()

        consultant = Consultant.get_by_id(consultant_id)

        if not consultant:
            return dict(status="fail", message=f"Consultant with id {consultant_id} not found"), 404

        consultant_data, errors = schema.dumps(consultant)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(consultant=json.loads(consultant_data))), 200

    def patch(self, consultant_id):
        """
        Update a single consultant
        """

        # To do check if user is admin
        schema = ConsultantSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        consultant = Consultant.get_by_id(consultant_id)

        if not consultant:
            return dict(status="fail", message=f"Consultant with id {consultant_id} not found"), 404

        updated_consultant = Consultant.update(consultant, **validated_update_data)

        if not updated_consultant:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Consultant updated successfully"), 200

    def delete(self, consultant_id):
        """
        Delete a single consultant
        """

        consultant = Consultant.get_by_id(consultant_id)

        if not consultant:
            return dict(status="fail", message=f"Consultant with id {consultant_id} not found"), 404

        deleted_consultant = consultant.delete()

        if not deleted_consultant:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
