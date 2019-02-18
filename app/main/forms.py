from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
	title = StringField('Comment title',validators=[Required()])

	comment = TextAreaField('blog comment', validators=[Required()])

	submit = SubmitField('Submit')

class BlogForm(FlaskForm):
	post = StringField('Topic',validators=[Required()])
	body = TextAreaField('blog')

	submit = SubmitField('blog')