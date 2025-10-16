from flask import Flask, render_template
import requests
app = Flask(__name__)

NASA_API = "vX5DDCbatnoXaTbA21tHG86AYxoHSXTdPLZ0GI7H"
URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API}"


@app.route("/", methods=["GET"])
def index():
    response = requests.get(URL)
    data = response.json()
    # print(data)
    return render_template("index.html", apod_data=data)

@app.route("/display", methods=["GET"])
def display():
    return ["Syed Umar Ali", "20-AI 4A"]

@app.route("/displayjson", methods=["GET"])
def displayjson():
    return {"Name":"Syed Umar Ali", 
            "Roll":"20-AI 4A"}

if __name__ == "__main__":
    app.run(debug=True)


