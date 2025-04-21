from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nearest_mbta", methods=["POST"])
def nearest_mbta():
    place = request.form.get("place")
    if not place:
        return render_template("error.html", message="Please enter a place name.")
    try:
        stop, wheelchair = find_stop_near(place)
        return render_template("mbta_station.html", stop=stop, wheelchair=wheelchair)
    except Exception as e:
        return render_template("error.html", message=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
