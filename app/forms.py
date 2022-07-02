from flask_wtf import FlaskForm
from wtforms.validators import data_required, ValidationError
from wtforms import StringField, SubmitField, EmailField, TelField, URLField
from flask_wtf.file import FileField


class AddNewBusiness(FlaskForm):
	name = StringField('name', validators=[data_required()])
	category = StringField('category', validators=[data_required()])
	phone = TelField('phone', validators=[data_required()])
	email = EmailField('email')
	website = URLField('website')
	facebook = URLField('facebook')
	address = StringField('address')
	sentence = StringField('about')
	submit = SubmitField('Create your business card now')

