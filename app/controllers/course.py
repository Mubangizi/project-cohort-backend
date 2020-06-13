import json
from flask_restful import Resource, request

from app.schemas import CourseSchema
from app.models.course import Course



class CourseView(Resource):

    def post(self):
        """
        Creating an Course ad
        """
        course_schema = CourseSchema()

        course_data = request.get_json()

        validated_course_data, errors = course_schema.load(course_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        course = Course(**validated_course_data)

        saved_course = course.save()

        if not saved_course:
            return dict(status='fail', message='Internal Server Error'), 500

        new_course_data, errors = course_schema.dumps(course)

        return dict(status='success', data=dict(course=json.loads(new_course_data))), 201

    # @jwt_required
    def get(self):
        """
        Getting All courses
        """

        course_schema = CourseSchema(many=True)

        courses = Course.find_all()

        courses_data, errors = course_schema.dumps(courses)

        if errors:
            return dict(status="fail", message="Internal Server Error"), 500

        return dict(status="success", data=dict(courses=json.loads(courses_data))), 200


class CourseDetailView(Resource):

    def get(self, course_id):
        """
        Getting individual course
        """
        schema = CourseSchema()

        course = Course.get_by_id(course_id)

        if not course:
            return dict(status="fail", message=f"Course with id {course_id} not found"), 404

        course_data, errors = schema.dumps(course)

        if errors:
            return dict(status="fail", message=errors), 500

        return dict(status='success', data=dict(course=json.loads(course_data))), 200

    def patch(self, course_id):
        """
        Update a single course
        """

        # To do check if user is admin
        schema = CourseSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        course = Course.get_by_id(course_id)

        if not course:
            return dict(status="fail", message=f"Course with id {course_id} not found"), 404

        updated_course = Course.update(course, **validated_update_data)

        if not updated_course:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message="Course updated successfully"), 200

    def delete(self, course_id):
        """
        Delete a single course
        """

        course = Course.get_by_id(course_id)

        if not course:
            return dict(status="fail", message=f"Course with id {course_id} not found"), 404

        deleted_course = course.delete()

        if not deleted_course:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
