import json
from flask_restful import Resource, request

from app.schemas import TicketSchema
from app.models.ticket import Ticket



class TicketView(Resource):

    def post(self):
        """
        Creating an Ticket ad
        """
        ticket_schema = TicketSchema()

        ticket_data = request.get_json()

        validated_ticket_data, errors = ticket_schema.load(ticket_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        ticket = Ticket(**validated_ticket_data)

        saved_ticket = ticket.save()

        if not saved_ticket:
            return dict(status='fail', message='Internal Server Error'), 500

        new_ticket_data, errors = ticket_schema.dumps(ticket)

        return dict(status='success', data=dict(ticket=json.loads(new_ticket_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All tickets
        """

        ticket_schema = TicketSchema(many=True)

        tickets = Ticket.find_all()

        tickets_data, errors = ticket_schema.dumps(tickets)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(tickets=json.loads(tickets_data))), 200


class TicketDetailView(Resource):

    def get(self, ticket_id):
        """
        Getting individual ticket
        """
        schema = TicketSchema()

        ticket = Ticket.get_by_id(ticket_id)

        if not ticket:
            return dict(status="fail", message=f"Ticket with id {ticket_id} not found"), 404

        ticket_data, errors = schema.dumps(ticket)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(ticket=json.loads(ticket_data))), 200

    def patch(self, ticket_id):
        """
        Update a single ticket
        """

        # To do check if ticket is admin
        schema = TicketSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        ticket = Ticket.get_by_id(ticket_id)

        if not ticket:
            return dict(status="fail", message=f"Ticket with id {ticket_id} not found"), 404

        updated_ticket = Ticket.update(ticket, **validated_update_data)

        if not updated_ticket:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Ticket updated successfully"), 200

    def delete(self, ticket_id):
        """
        Delete a single ticket
        """

        ticket = Ticket.get_by_id(ticket_id)

        if not ticket:
            return dict(status="fail", message=f"Ticket with id {ticket_id} not found"), 404

        deleted_ticket = ticket.delete()

        if not deleted_ticket:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
