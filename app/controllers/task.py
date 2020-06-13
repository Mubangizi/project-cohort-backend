import json
from flask_restful import Resource, request

from app.schemas import TaskSchema
from app.models.task import Task



class TaskView(Resource):

    def post(self):
        """
        Creating an Task ad
        """
        task_schema = TaskSchema()

        task_data = request.get_json()

        validated_task_data, errors = task_schema.load(task_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        task = Task(**validated_task_data)

        saved_task = task.save()

        if not saved_task:
            return dict(status='fail', message='Internal Server Error'), 500

        new_task_data, errors = task_schema.dumps(task)

        return dict(status='success', data=dict(task=json.loads(new_task_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All tasks
        """

        task_schema = TaskSchema(many=True)

        tasks = Task.find_all()

        tasks_data, errors = task_schema.dumps(tasks)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(tasks=json.loads(tasks_data))), 200


class TaskDetailView(Resource):

    def get(self, task_id):
        """
        Getting individual task
        """
        schema = TaskSchema()

        task = Task.get_by_id(task_id)

        if not task:
            return dict(status="fail", message=f"Task with id {task_id} not found"), 404

        task_data, errors = schema.dumps(task)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(task=json.loads(task_data))), 200

    def patch(self, task_id):
        """
        Update a single task
        """

        # To do check if user is admin
        schema = TaskSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        task = Task.get_by_id(task_id)

        if not task:
            return dict(status="fail", message=f"Task with id {task_id} not found"), 404

        updated_task = Task.update(task, **validated_update_data)

        if not updated_task:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Task updated successfully"), 200

    def delete(self, task_id):
        """
        Delete a single task
        """

        task = Task.get_by_id(task_id)

        if not task:
            return dict(status="fail", message=f"Task with id {task_id} not found"), 404

        deleted_task = task.delete()

        if not deleted_task:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
