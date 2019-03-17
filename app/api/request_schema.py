"""
    Request Schema
"""
from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage

class UserRequestSchema:
    """Define all mandatory argument for creating user"""
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str)
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("password",type=str, required=True)
#end class