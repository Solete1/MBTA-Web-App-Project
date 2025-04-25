from flask import Flask, render_template, request
from mbta_helper import find_place_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    place_name = request.form.get('place')
    if not place_name:
        return render_template('error.html', message="No place name provided.")

    try:
        station, wheelchair_accessible, weather, events = find_place_info(place_name)
        return render_template(
            'mbta_station.html',
            place=place_name,
            station=station,
            accessible="Yes" if wheelchair_accessible == "Yes" else "No",
            weather=weather,
            events=events
        )
    except Exception as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
