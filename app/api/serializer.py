"""
    Serializer & Deserialize
"""
from marshmallow import fields
from marshmallow import ValidationError
from marshmallow import validates
from marshmallow import post_load

from app.api import ma

def cannot_be_blank(string):
    """
        function to make user not enter empty string
        args :
            string -- user inputted data
    """
    if not string:
        raise ValidationError("Data cannot be blank")
#end def

class UserSchema(ma.Schema):
    """ this is class schema for User"""
    id = fields.Str()
    name = fields.Str()
    username = fields.Str(required=True, validate=cannot_be_blank, allow_none=True)
    password = fields.Str(required=True, validate=cannot_be_blank, load_only=True)
    created_at = fields.DateTime('%Y-%m-%d %H:%M:%S')
