from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms import EmailField
from wtforms import validators

class diccionarioForm(Form):
    ingles = StringField("Ingles", [validators.DataRequired(message="el campo es requerido"), 
                         validators.length(min=2, max=10, message="ingresa nombre valido")])
    español = StringField("Español", [validators.DataRequired(message="el campo es requerido"), 
                         validators.length(min=2, max=10, message="ingresa nombre valido")])
    buscar = StringField("Palabra", [validators.DataRequired(message="el campo es requerido"), 
                         validators.length(min=2, max=10, message="ingresa nombre valido")])
    radio = RadioField(choices=[('español','Español'), ('ingles','Ingles')])