from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lenght", methods =["GET","POST"])
def lenght():
    result = None
    
    #wyciaganie z htmla z metody post
    if request.method == "POST":
        value = float(request.form["value"])
        unit_from = request.form["from"]
        unit_to = request.form["to"]

        # dict okreslajacy nasze jednostki (bazujacy na metrze)
        conversions = {
            "mm" : 0.001,
            "cm" : 0.01,
            "m" : 1,
            "km" : 1000,
            "inch" : 0.0254,
            "foot" : 0.3048,
            "yard" : 0.9144,
            "mile" : 1609.34
        }

        #konwersja najpierw na metr, a potem na docelowe jednostki
        value_to_meter = value * conversions[unit_from]
        result = value_to_meter / conversions[unit_to]

    # render temolate wrzuca nam cos do folderu template, tutaj to co podamy. result = result potrzebne, bo pierwsze name to nazwa zmiennej w pliku a html, a druga to ta z tego pliku.
    return render_template("lenght.html", result = result)

@app.route("/weight", methods =["GET","POST"])
def weight():
    result = None
    
    #wyciaganie z htmla z metody post
    if request.method == "POST":
        value = float(request.form["value"])
        unit_from = request.form["from"]
        unit_to = request.form["to"]

        # dict okreslajacy nasze jednostki (bazujacy na gramie)
        conversions = {
            "mg" : 0.001,
            "g" : 1,
            "kg" : 1000,
            "oz" : 28.34952,
            "lb" : 453.59237,
        }

        #konwersja najpierw na gram, a potem na docelowe jednostki
        value_to_gram = value * conversions[unit_from]
        result = value_to_gram / conversions[unit_to]

    # render temolate wrzuca nam cos do folderu template, tutaj to co podamy. result = result potrzebne, bo pierwsze name to nazwa zmiennej w pliku a html, a druga to ta z tego pliku.
    return render_template("weight.html", result = result)
