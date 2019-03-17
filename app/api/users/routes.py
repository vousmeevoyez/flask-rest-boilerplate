"""
    Routes
    ___________
    this is where our flask app define all url
"""
from flask import request
from flask_restplus import Resource

from app.api.users import api
from app.api.request_schema import UserRequestSchema
from app.api.users.services.user_services import UserServices

request_schema = UserRequestSchema.parser

@api.route("/")
class UserRoutes(Resource):
    """
        user routes
        api/v1/users/
    """
    def get(self):
        """
            Handle GET HTTP Method
        """
        username = request.args.get('username')
        response = UserServices().get(username)
        return response

    def post(self):
        """
            Handle POST HTTP Method
        """
        request_data = request_schema.parse_args(strict=True)
        response = UserServices().add(request_data)
        return response