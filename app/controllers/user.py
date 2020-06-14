import json
from flask_restful import Resource, request

from app.schemas import UserSchema
from app.models.user import User



class UserView(Resource):

    def post(self):
        """
        Creating an User ad
        """
        user_schema = UserSchema()

        user_data = request.get_json()

        validated_user_data, errors = user_schema.load(user_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        user = User(**validated_user_data)

        saved_user = user.save()

        if not saved_user:
            return dict(status='fail', message='Internal Server Error'), 500

        new_user_data, errors = user_schema.dumps(user)

        return dict(status='success', data=dict(user=json.loads(new_user_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All users
        """

        user_schema = UserSchema(many=True)

        users = User.find_all()

        users_data, errors = user_schema.dumps(users)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(users=json.loads(users_data))), 200


class UserDetailView(Resource):

    def get(self, user_id):
        """
        Getting individual user
        """
        schema = UserSchema()

        user = User.get_by_id(user_id)

        if not user:
            return dict(status="fail", message=f"User with id {user_id} not found"), 404

        user_data, errors = schema.dumps(user)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(user=json.loads(user_data))), 200

    def patch(self, user_id):
        """
        Update a single user
        """

        # To do check if user is admin
        schema = UserSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        user = User.get_by_id(user_id)

        if not user:
            return dict(status="fail", message=f"User with id {user_id} not found"), 404

        updated_user = User.update(user, **validated_update_data)

        if not updated_user:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="User updated successfully"), 200

    def delete(self, user_id):
        """
        Delete a single user
        """

        user = User.get_by_id(user_id)

        if not user:
            return dict(status="fail", message=f"User with id {user_id} not found"), 404

        deleted_user = user.delete()

        if not deleted_user:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
