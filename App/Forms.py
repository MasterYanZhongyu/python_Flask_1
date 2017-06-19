from flask_wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,length

class NameForm(Form):
    name=StringField('What is your name?',validators=[DataRequired()])
    remark=TextAreaField("input remarks!")
    submit=SubmitField('Submit')
