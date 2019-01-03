from flask_wtf import FlaskForm
from wtforms import StringField
from wtfoorms.validators import DataRequired

class Letters(FlaskForm):
    A = StringField("A", validators = [DataRequired()])
    B = StringField("B", validators = [DataRequired()])
    A = StringField("A", validators = [DataRequired()])

class Form(FlaskForm):
    course = StringField("Course", validators=[DataRequired()])
    part_1 = StringField("Component and Percentage 1", validators=[DataRequired()])
    part_2 = StringField("Component and Percentage 2")
    part_3 = StringField("Component and Percentage 3")
    part_4 = StringField("Component and Percentage 4")
    part_5 = StringField("Component and Percentage 5")
    
