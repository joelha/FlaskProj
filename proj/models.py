from flask.ext.login import UserMixin

class User(UserMixin):

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def get_id(self):
		return unicode(self.username)