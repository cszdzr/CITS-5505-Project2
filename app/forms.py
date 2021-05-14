from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class RPPForm(FlaskForm):
    question1 = RadioField('How big must the parking spot be for you to be able to fit into it easily?', choices=[(1,'A) 1 times the length of your car'),(2,'B) 1.5 times the length of your car'),(3,'C) 2 times the length of your car')], validators=[DataRequired()])
    question2 = RadioField('When should you initially start turning into the parking space?', choices=[(1,'A) Before the back end of the front car is visible in the triangular window'),(2,'B) When the back end of the front car is visible in the triangular window'),(3,'C) After the back end of the front car has completely left the triangular window')], validators=[DataRequired()])
    question3 = RadioField('When should you return the steering wheel to straight?', choices=[(1,'A) When the right hand corner of the back car appears in the left hand mirror'),(2,'B) When the middle of the back car appears in the left hand mirror'),(3,'C) When you feel the wheels hit the curb')], validators=[DataRequired()])
    question4 = RadioField('When should you turn the steering wheel to the left?', choices=[(1,'A) When the right hand mirror covers the left hand tail light of the car in front'),(2,'B) When the right hand mirror covers the number plate of the car in front'),(3,'C) When the back of your car is about 50 cm from the curb')], validators=[DataRequired()])
    question5 = RadioField('When should you return the steering wheel to a straight position?', choices=[(1,'A) When your car is within 10 cm of the curb'),(2,'B) When your car is about 30 cm behind the car in front'),(3,'C) When your right hand mirror shows that you are parallel to the curb')], validators=[DataRequired()])
    submit = SubmitField('Submit')
