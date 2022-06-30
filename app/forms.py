from flask_wtf import FlaskForm
from wtforms.validators import data_required, ValidationError
from wtforms import StringField, SubmitField, EmailField, TelField, URLField, PasswordField
from flask_wtf.file import FileField


class AddNewBusiness(FlaskForm):
	name = StringField('name of business', validators=[data_required()])
	category = StringField('category', validators=[data_required()])
	phone = TelField('phone number', validators=[data_required()])
	email = EmailField('email')
	website = URLField('website')
	facebook = URLField('facebook page')
	address = StringField('address')
	sentence = StringField('killer sentence about')
	submit = SubmitField('Create your business card now')

