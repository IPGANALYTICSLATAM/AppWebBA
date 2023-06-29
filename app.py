from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Bogota123$"

@app.route("/hello")   # ultima parte del url
def index():
    flash("cual es tu name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", que bueno verte mi perro salchicha")
    return render_template("index.html")