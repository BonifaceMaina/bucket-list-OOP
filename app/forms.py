from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators
from wtforms.validators import Length, DataRequired

class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=4, max=16)])
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=16)])
    password = PasswordField('Password',  [validators.DataRequired(), validators.EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('confirm_password')

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class BucketlistForm(FlaskForm):
    bucketlist = StringField("Name", validators=[DataRequired()])

class BucketlistItems(FlaskForm):
    bucketitem = StringField("Name", validators=[DataRequired()])
    
class EditBucketListForm(FlaskForm):
    value = StringField("Name", [validators.DataRequired()])
    
class EditBucketListItemsForm(FlaskForm):
    value = StringField("Name", [validators.DataRequired()])