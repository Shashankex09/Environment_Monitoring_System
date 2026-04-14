from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)

# Store historical data
MAX_POINTS = 50
pollution_data = deque(maxlen=MAX_POINTS)
temperature_data = deque(maxlen=MAX_POINTS)
humidity_data = deque(maxlen=MAX_POINTS)

latest_pollution = 0
latest_temperature = 0
latest_humidity = 0


@app.route('/')
def home():
    return render_template('index.html')


# Endpoint for ESP32 to send data
@app.route('/data')
def receive_data():
    global latest_pollution, latest_temperature, latest_humidity

    pollution = request.args.get('pollution')
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity')

    if pollution is not None:
        latest_pollution = int(float(pollution))
        pollution_data.append(latest_pollution)

    if temperature is not None:
        latest_temperature = float(temperature)
        temperature_data.append(latest_temperature)

    if humidity is not None:
        latest_humidity = float(humidity)
        humidity_data.append(latest_humidity)

    return jsonify({
        "status": "success",
        "pollution": latest_pollution,
        "temperature": latest_temperature,
        "humidity": latest_humidity,
        "danger": latest_pollution > 1000
    })


# Endpoint for dashboard to fetch latest data
@app.route('/latest')
def latest():
    return jsonify({
        "pollution": latest_pollution,
        "temperature": latest_temperature,
        "humidity": latest_humidity,
        "pollution_history": list(pollution_data),
        "temperature_history": list(temperature_data),
        "humidity_history": list(humidity_data),
        "danger": latest_pollution > 1000
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)