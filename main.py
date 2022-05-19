from flask import Flask, request
from api_client import build_weather_query, get_weather_data

app = Flask(__name__)

@app.route('/get-weather-data', methods=['POST'])
def display_weather_info():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.get_json()
        city_input = json_data["city"]
        imperial = json_data["imperial"]

        url = build_weather_query(city_input, imperial)
        weather_data = get_weather_data(url)

        return weather_data

if __name__ == '__main__':
    app.run(debug=True)