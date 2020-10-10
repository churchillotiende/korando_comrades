from flask_wtf import  FlaskForm
from flask_wtf.file import FileField , FileAllowed
from flask_login import current_user
from flask_blog.models import User , Post
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField
from wtforms.validators import DataRequired , Length , EqualTo , Email , ValidationError
# for you to create a form in flask you have to create a class for that form

class RegistrationForm(FlaskForm):
    username = StringField('Username' ,
                         validators = [DataRequired() , Length(min = 2 , max = 20)])
    email = StringField('Email' , 
                        validators = [DataRequired() , Email()])
    password = PasswordField('Password' , 
                        validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password' , 
                        validators = [DataRequired() , EqualTo('password')])
    submit = SubmitField('Sign Up' )

    def validate_username(self , username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is taken please choose a different one')

     
    def validate_email(self , email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('That email is taken please choose a different one')

class LoginForm(FlaskForm):
   
    email = StringField('Email' , 
                        validators = [DataRequired() , Email()])
    password = PasswordField('Password' , 
                        validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username' ,
                        validators = [DataRequired() , Length(min = 2 , max = 20)])
    email = StringField('Email' , 
                        validators = [DataRequired() , Email()])

    picture = FileField("Update you profile picture" , validators = [FileAllowed(['jpg' , 'png'])])
    submit = SubmitField('Update' )

    def validate_username(self , username):
        if username.data != current_user.username:
                user = User.query.filter_by(username = username.data).first()
                if user:
                    raise ValidationError('That username is taken please choose a different one')

     
    def validate_email(self , email):
         if email.data != current_user.email:
                user = User.query.filter_by(email = email.data).first()
                if user:
                    raise ValidationError('That email is taken please choose a different one')
class PostForm(FlaskForm):
    title = StringField('Title' , validators = [DataRequired()])
    content = TextAreaField('Content' , validators = [DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email' , 
                          validators = [DataRequired() , Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self , email):
        user = User.query.filter_by(email  =email.data).first()
        if user is None:
            raise ValidationError('That email doesnt exist you have to register first')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password' , validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password' , 
                                                        validators = [DataRequired() , EqualTo('password')])
    submit = SubmitField('Reset password')