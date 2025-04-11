import requests

API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        weather = {
            "City": data["name"],
            "Temperature": data["main"]["temp"],
            "Feels Like": data["main"]["feels_like"],
            "Humidity": data["main"]["humidity"],
            "Description": data["weather"][0]["description"].capitalize()
        }

        return weather

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
    except KeyError:
        print("Invalid response received.")
        return None

def display_weather(info):
    print("\n🌤️ Weather Info:")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print("📍 Weather Checker")
    city = input("Enter a city name: ")
    weather_info = get_weather(city)

    if weather_info:
        display_weather(weather_info)
    else:
        print("❌ Could not retrieve weather info.")
