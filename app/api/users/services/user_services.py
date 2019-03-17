"""
	User Services
"""

from app.api.models import User
from app.api.serializer import UserSchema

class UserServices:

	def add(self, request_data):
		response = {
			"message" : "Successfully add user!"
		}
		user = User(**request_data)
		user.save()
		return response

	def get(self, username):
		user = User.objects(username=username).first()
		response = UserSchema().dump(user).data
		return response