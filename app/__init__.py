""" 
    Package Initialization
"""

from flask_restplus import Api

from flask import Blueprint

from app.api.users import api as user_ns


blueprint = Blueprint("api", __name__)
# intialize API
api = Api(blueprint, contact="kelvindsmn@gmail.com")# register blueprint
api.add_namespace(user_ns, path="/users")