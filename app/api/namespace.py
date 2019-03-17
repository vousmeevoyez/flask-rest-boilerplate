""" 
    Flask Restplus Namespace
"""
from flask_restplus import Namespace

class UserNamespace:
    api = Namespace("users")
#end class