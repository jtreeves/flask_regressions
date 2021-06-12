from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email
from email_validator import validate_email
from .models import User

class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    key = HiddenField(validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        found_user = User.query.filter_by(
            email = email.data
        ).first()
        if found_user:
            raise ValidationError()