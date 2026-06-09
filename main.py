from flask import Flask
app = Flask(__name__)

@app.route("/")

def home():
    return "Dobar dan pocetna stranica"

@app.route("/kontakt")

def contact():
    return "Moj broj je 555 333"

if __name__ == "__main__":
    app.run(debug=True)