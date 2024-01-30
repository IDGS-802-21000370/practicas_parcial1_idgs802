from flask import Flask, request, render_template
import distancia
import forms
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout2.html")


@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


@app.route("/hola")
def func():
    return "<p> Saludo desde hola -UTL <p>"


@app.route("/saludo")
def func1():
    return "<p> Saludo desde Saludo <p>"


@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1>Hola </h1>"+nom


@app.route("/numero/<int:n1>")
def numero(n1):
    return "<h1>El valor es {}</h1>".format(n1)

@app.route("/user/<string:nom>/<int:id>")
def user(id,nom):
    return "<h1> ID: {} NOMBRE: {}</h1>".format(id,nom)


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "<h1>La suma de {} + {} = {}</h1>".format(n1,n2,n1+n2)



@app.route("/multiplica", methods=["GET", "POST"])
def mult():
    if request.method=="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return"<h1> El resultado es: {}</h1>".format(int(num1) * int(num2))        
    else:
        return """
                    <form action="/multiplica" method="POST">
                        <label>N1:</label>
                        <input type="text" name="n1"/>
                        <label>N2:</label>
                        <input type="text" name="n2"/>
                        <input type="submit"/>
                    </form>
                """
    
@app.route("/formulario1", methods=["GET", "POST"])
def calculo():
    return render_template('formulario1.html')

@app.route("/resultado", methods=["GET", "POST"])
def operacionesBasicas():
    if request.method == "POST":
        if request.form['elegir'] == 'Sumar':
            num1 = int(request.form.get("n1"))
            num2 = int(request.form.get("n2"))
            r = num1 + num2
        elif request.form['elegir'] == 'Restar':
            num1 = int(request.form.get("n1"))
            num2 = int(request.form.get("n2"))
            r = num1 - num2
        elif request.form['elegir'] == 'Multiplicar':
            num1 = int(request.form.get("n1"))
            num2 = int(request.form.get("n2"))
            r = num1 * num2
        elif request.form['elegir'] == 'Dividir':
                num1 = int(request.form.get("n1"))
                num2 = int(request.form.get("n2"))
                if num2 != 0:
                    r = num1 / num2
                else:
                    return "No se puede dividir"
        else:
            return "No se puede hacer la operacion"

    return render_template('formulario1.html', resultado=r)


@app.route("/distancia", methods=["GET", "POST"])
def diatancia():
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    r = ""
    distancia_form=forms.UserForm(request.form)
    if request.method == "POST":
        x1 = float(distancia_form.x1.data)
        y1 = float(distancia_form.y1.data)
        x2 = float(distancia_form.x2.data)
        y2 = float(distancia_form.y2.data)
        funcion = distancia.DistanciaNumeros(x1,y1,x2,y2)
        r = float(funcion.formula_distancia())
        print("x1: {}".format(x1))
        print("y2: {}".format(y1))
        print("x2: {}".format(x2))
        print("y2: {}".format(y2))
        
    return render_template('formularioDistancia.html', form=distancia_form, x1=x1, y1=y1, x2=x2, y2=y2, resultado=r)

if __name__ == "__main__":
    app.run(debug=True)


