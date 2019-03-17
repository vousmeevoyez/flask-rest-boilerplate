"""
    Document Models
"""
from mongoengine import *

class User(Document):
    name = StringField(required=True, max_length=200)
    username = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
