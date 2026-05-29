import requests

def get_weather(latitude, longitude, city_name):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "hourly": "temperature_2m,weather_code",
        "forecast_days": 1,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        current = data["current"]

        print(f"Current weather in {city_name}:")
        print(f"Temperature: {current['temperature_2m']}°C")
        print(f"Wind Speed: {current['wind_speed_10m']} km/h")
        print(f"Weather Code: {current['weather_code']}")

        print("\n Hourly forecast (next 24 hours): ")
        hours = data["hourly"]["time"][:24]
        temperatures = data["hourly"]["temperature_2m"][:24]
        weather_codes = data["hourly"]["weather_code"][:24]

        for time, temp, code in zip(hours, temperatures, weather_codes):
            print(f"{time}: {temp}°C, Weather Code: {code}")
            return data
    except requests.exceptions.ConnectionError:
        print("No Internet connection. Please check your network settings.")
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def main():
    while True:
        print("\n--- Get Weather Information ---")
        city_name = input("Enter city name (or 'quit' to exit): ").strip()
        
        if city_name.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            
            get_weather(latitude, longitude, city_name)
        except ValueError:
            print("Invalid input. Please enter valid numbers for latitude and longitude.")


if __name__ == "__main__":
    main()