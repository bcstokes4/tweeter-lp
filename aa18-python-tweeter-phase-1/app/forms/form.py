from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class Tweet(FlaskForm):
    author = StringField("Author:")
    tweet = StringField("Tweet")
    submit = SubmitField("Create Tweet")