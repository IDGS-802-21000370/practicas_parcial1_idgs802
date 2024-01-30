from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms import EmailField

class UserForm(Form):
    x1 = StringField("x1")
    y1 = StringField("y1")
    x2 = StringField("x2")
    y2 = StringField("y2")
    materias = SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','Ing')])
    radios = RadioField('Curso',choices=[("1", "1"),("2", "2"),("3", "3")])