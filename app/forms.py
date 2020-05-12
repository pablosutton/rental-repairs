from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class LandlordForm (FlaskForm):
    lln = StringField('Landlord name:', validators=[DataRequired()])
    lla = StringField('Landlord address:', validators=[DataRequired()])
    llsu = StringField('Landlord Suburb:', validators=[DataRequired()])
    llst = StringField('Landlord State:', validators=[DataRequired()])
    llpc = IntegerField('Landlord Postcode:', validators=[DataRequired()])
    submit = SubmitField('Create Notice')
