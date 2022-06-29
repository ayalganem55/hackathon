from flask_wtf import FlaskForm
from wtforms.validators import data_required
from wtforms import StringField, SubmitField, EmailField, FileField, TelField, URLField


class AddNewBusiness(FlaskForm):
	name = StringField('name of business', validators=[data_required()])
	category = StringField('category of business', validators=[data_required()])
	phone = TelField('phone number', validators=[data_required()])
	email = EmailField('email')
	website = URLField('website')
	facebook = URLField('facebook page')
	address = StringField('address')
	sentence = StringField('killer sentence about')
	submit = SubmitField('Create your business card now')
