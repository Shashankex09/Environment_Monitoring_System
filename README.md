# Environment Monitoring System

Environment Monitoring System is a Flask-based web dashboard for tracking live environmental readings. It receives pollution, temperature, and humidity values from a device such as an ESP32, stores a short in-memory history, and displays the data on a browser dashboard with charts.

## Overview

This project is designed for simple real-time monitoring. The backend accepts sensor readings through a request endpoint and keeps the latest values available for the frontend. The dashboard then polls the backend regularly and updates the charts without needing a page reload.

## Features

- Live dashboard for pollution, temperature, and humidity readings
- Combined chart for comparing multiple sensor values together
- Separate charts for each metric
- Lightweight Flask backend
- Endpoint for receiving device data
- Endpoint for retrieving the latest values and history
- In-memory storage for recent sensor points

## Project Structure

```text
Environment_monitoring/
|-- src/
|   |-- server.py
|   |-- static/
|   |   |-- combined.png
|   |   |-- graph.png
|   |   |-- humidity.png
|   |   |-- pollution.png
|   |   `-- temperature.png
|   `-- templates/
|       `-- index.html
|-- .gitignore
|-- README.md
|-- push.bat
`-- requirements.txt
```

## Technology Used

- Python 3
- Flask
- HTML, CSS, and JavaScript
- Chart.js

## Requirements

Before running the project, make sure you have:

- Python 3 installed
- `pip` available in your Python environment
- Flask installed through `requirements.txt`

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Start the Flask application with:

```bash
python src/server.py
```

By default, the application runs at:

```text
http://127.0.0.1:5000
```

## How It Works

1. A sensor device sends pollution, temperature, and humidity values to the `/data` endpoint.
2. The Flask backend stores the latest values and appends them to short history buffers.
3. The frontend dashboard requests the latest data from `/latest`.
4. The charts refresh automatically to show the newest readings.

## API Endpoints

### `GET /`

Loads the main dashboard page.

### `GET /data`

Receives sensor values through query parameters.

Supported query parameters:

- `pollution`
- `temperature`
- `humidity`

Example request:

```text
/data?pollution=320&temperature=29.5&humidity=68
```

Example response:

```json
{
  "status": "success",
  "pollution": 320,
  "temperature": 29.5,
  "humidity": 68,
  "danger": false
}
```

### `GET /latest`

Returns the latest values and recent history for dashboard charts.

Example response:

```json
{
  "pollution": 320,
  "temperature": 29.5,
  "humidity": 68,
  "pollution_history": [300, 305, 320],
  "temperature_history": [28.9, 29.1, 29.5],
  "humidity_history": [66, 67, 68],
  "danger": false
}
```

## Notes

- The application stores history in memory using Python `deque`.
- The current maximum number of stored points is `50`.
- A danger flag becomes `true` when pollution is greater than `1000`.
- The current server configuration uses `debug=True`.

## Git Helper

The included `push.bat` file can be used to quickly stage, commit, and push changes from Windows.

## Future Improvement Ideas

- Save sensor history in a database
- Add authentication for write endpoints
- Validate incoming sensor values more strictly
- Improve dashboard styling and text encoding
- Add deployment instructions for cloud hosting
