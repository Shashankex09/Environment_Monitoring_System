# Environment Monitoring System

An environmental monitoring dashboard built with Flask for displaying live pollution, temperature, and humidity readings.

## Features

- Live dashboard for pollution, temperature, and humidity
- Combined graph for all sensor streams
- Individual charts for each metric
- Simple API endpoint for incoming sensor data
- Latest data endpoint for dashboard refreshes

## Project Structure

```text
Environment_monitoring/
|-- src/
|   |-- server.py
|   |-- static/
|   `-- templates/
|       `-- index.html
|-- .gitignore
|-- README.md
|-- push.bat
`-- requirements.txt
```

## Requirements

- Python 3.x
- Flask

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python src/server.py
```

The app runs on:

```text
http://127.0.0.1:5000
```

## API Endpoints

### `GET /`

Loads the environmental monitoring dashboard.

### `GET /data`

Receives sensor values through query parameters.

Example:

```text
/data?pollution=320&temperature=29.5&humidity=68
```

### `GET /latest`

Returns the latest dashboard values and chart history in JSON format.

## Notes

- The dashboard stores recent readings in memory.
- The application is currently configured to run with `debug=True`.
