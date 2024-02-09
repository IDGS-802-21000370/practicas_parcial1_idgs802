from wtforms import Form
from wtforms import SelectField, RadioField
from wtforms import EmailField

class resistenciasForm(Form):
    color1 = SelectField('Color1', choices=[('Negro','Negro'),('Cafe','Cafe'),('Rojo','Rojo'),('Naranja','Naranja'),('Amarillo','Amarillo'),('Verde','Verde'),('Azul','Azul'),('Violeta','Violeta'),('Gris','Gris'),('Blanco','Blanco')])
    color2 = SelectField('Color1', choices=[('Negro','Negro'),('Cafe','Cafe'),('Rojo','Rojo'),('Naranja','Naranja'),('Amarillo','Amarillo'),('Verde','Verde'),('Azul','Azul'),('Violeta','Violeta'),('Gris','Gris'),('Blanco','Blanco')])
    color3 = SelectField('Color1', choices=[('Negro','Negro'),('Cafe','Cafe'),('Rojo','Rojo'),('Naranja','Naranja'),('Amarillo','Amarillo'),('Verde','Verde'),('Azul','Azul'),('Violeta','Violeta'),('Gris','Gris'),('Blanco','Blanco')])
    radios = RadioField('Radios',choices=[(0.10, "Oro"), (0.05, "Plata")])

