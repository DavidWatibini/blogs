from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id  = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(255))
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
	email = db.Column(db.String(255),unique = True,index = True)
	password_hash = db.Column(db.String(255))
	pass_secure = db.Column(db.String(255))
	blogs = db.relationship('Blog',backref='blogs',lazy="dynamic")
	# comments = db.relationship('Comment',backref='comments',lazy="dynamic")

	@property
	def password(self):

		raise AttributeError('Cant read')

	@password.setter
	def password(self,password):

		self.pass_secure = generate_password_hash(password)

	def  verify_password(self,password):
		return check_password_hash(self.pass_secure,password)

		

	def __repr__(self):

		return f'User {self.username}'

class Role(db.Model):
	__tablename__ = 'roles'

	id  = db.Column(db.Integer,primary_key =True)
	name= db.Column(db.String(255))
	user_id = db.relationship('User',backref = 'role',lazy="dynamic")

	def __repr__(self):

		return f'User {self.name}'

class Blog(UserMixin,db.Model):

	__tablename__ = 'blogs'

	id = db.Column(db.Integer,primary_key=True)
	post = db.Column(db.String(255))
	body = db.Column(db.String(1000))
	category = db.Column(db.String(1000))
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
	# comments = db.relationship('Comment',backref = 'blog',lazy = "dynamic")

	def save_blog(self):
		db.session.add(self)
		db.session.commit()

# class Comment(UserMixin,db.Model):
# 	"""docstring for Comment"""
# 	__tablename__ = 'comments'
# 	id = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.String(255))
# 	comments = db.Column(db.String(1000))
# 	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
# 	blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
# 	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


	def save_comment(self):
		db.session.add(self)
		db.session.commit()


class Popular:

	'''
	News class to define Objects
	'''
	def __init__(self, author, quote):


		self.author = author
		self.quote = quote
