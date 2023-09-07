import requests

def get_weather_data():
    URL = "https://api.open-meteo.com/v1/forecast?latitude=17.384&longitude=78.4564&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,rain,visibility,windspeed_10m,winddirection_180m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max&current_weather=true&timezone=auto&forecast_days=1"

    response = requests.get(URL)

    if response.status_code != 200:
        raise Exception("Request Failed")
    return response.json()


def calculate_average(values):
    return sum(values) / len(values)


def format_time(date, time):
    time = time.replace(date, "")
    return time.replace("T", "")


def main():
    data = get_weather_data()

    current_weather = data["current_weather"]
    daily_data = data["daily"]
    hourly_data = data["hourly"]

    longitude = data["longitude"]
    latitude = data["latitude"]
    elevation = data["elevation"]
    timeZone = data["timezone"]
    date = daily_data["time"][0]

    current_time = format_time(date, current_weather["time"])
    current_temp = current_weather["temperature"]
    wind_speed = current_weather["windspeed"]
    rain = hourly_data["rain"]
    avg_rain = calculate_average(rain)
    uv_index = daily_data["uv_index_max"][0]
    sunrise = format_time(date, daily_data["sunrise"][0])
    sunset = format_time(date, daily_data["sunset"][0])
    max_temp = daily_data["temperature_2m_max"][0]
    min_temp = daily_data["temperature_2m_min"][0]
    visibility = hourly_data["visibility"]
    avg_visibility = calculate_average(visibility)


    print("======================WEATHER REPORT======================")
    print(f"Longitude: {longitude:.2f}")
    print(f"Latitude: {latitude:.2f}")
    print(f"Elevation: {elevation} metres")
    print(f"TimeZone: {timeZone}")
    print(f"Current Time: {current_time}")
    print(f"Date: {date}")
    print(f"Current Temp: {current_temp} °C")
    print(f"Maximum Temperature: {max_temp} °C")
    print(f"Minimum Temperature: {min_temp} °C")
    print(f"Average Rainfall: {avg_rain:.2f} mm")
    print(f"Wind Speed: {wind_speed} Km/h")
    print(f"UV Index: {uv_index}")
    print(f"Sunrise: {sunrise} a.m")
    print(f"Sunset: {sunset} p.m")
    print(f"Average Visibility: {avg_visibility:.2f} metres")
    print("==========================================================")

if __name__ == "__main__":
    main()