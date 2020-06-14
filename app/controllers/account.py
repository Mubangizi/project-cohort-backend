import json
from flask_restful import Resource, request

from app.schemas import AccountSchema
from app.models.account import Account



class AccountView(Resource):

    def post(self):
        """
        Creating an Account ad
        """
        account_schema = AccountSchema()

        account_data = request.get_json()

        validated_account_data, errors = account_schema.load(account_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        account = Account(**validated_account_data)

        saved_account = account.save()

        if not saved_account:
            return dict(status='fail', message='Internal Server Error'), 500

        new_account_data, errors = account_schema.dumps(account)

        return dict(status='success', data=dict(account=json.loads(new_account_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All accounts
        """

        account_schema = AccountSchema(many=True)

        accounts = Account.find_all()

        accounts_data, errors = account_schema.dumps(accounts)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(accounts=json.loads(accounts_data))), 200


class AccountDetailView(Resource):

    def get(self, account_id):
        """
        Getting individual account
        """
        schema = AccountSchema()

        account = Account.get_by_id(account_id)

        if not account:
            return dict(status="fail", message=f"Account with id {account_id} not found"), 404

        account_data, errors = schema.dumps(account)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(account=json.loads(account_data))), 200

    def patch(self, account_id):
        """
        Update a single account
        """

        # To do check if user is admin
        schema = AccountSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        account = Account.get_by_id(account_id)

        if not account:
            return dict(status="fail", message=f"Account with id {account_id} not found"), 404

        updated_account = Account.update(account, **validated_update_data)

        if not updated_account:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Account updated successfully"), 200

    def delete(self, account_id):
        """
        Delete a single account
        """

        account = Account.get_by_id(account_id)

        if not account:
            return dict(status="fail", message=f"Account with id {account_id} not found"), 404

        deleted_account = account.delete()

        if not deleted_account:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
